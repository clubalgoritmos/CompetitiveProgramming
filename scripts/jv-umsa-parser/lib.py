import os
import re
from typing import Dict, List, Tuple
from urllib.parse import parse_qs, urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


class Parser:
    def __init__(self, path: str = os.getcwd(), timeout: int = 20):
        self.path = path
        self.timeout = timeout
        self.indent_by_tag = {
            "h2": 1,
            "h3": 2,
            "span": 3,
            "p": 3,
            "pre": 3,
            "a": 1,
        }
        self.base_url = "https://jv.umsa.bo/oj/"
        os.makedirs(self.path, exist_ok=True)

    def _sanitize_text(self, text: str) -> str:
        cleaned = "".join(ch for ch in text.strip() if ch.isprintable())
        return re.sub(r"\s+", " ", cleaned)

    def _sanitize_filename(self, name: str) -> str:
        sanitized = re.sub(r'[\\/:*?"<>|]', "", name)
        sanitized = re.sub(r"\s+", "_", sanitized)
        sanitized = re.sub(r"_+", "_", sanitized)
        return sanitized.strip("_")

    def _request_soup(self, url: str) -> BeautifulSoup:
        response = requests.get(url, timeout=self.timeout)
        response.raise_for_status()
        return BeautifulSoup(response.content, "html.parser")

    def _get_attrs(self, element) -> Dict[str, str]:
        attrs = dict(element.attrs)
        attrs["text"] = self._sanitize_text(element.get_text())
        attrs["name"] = element.name
        return attrs

    def _get_content(self, url: str, query: str) -> List[Dict[str, str]]:
        soup = self._request_soup(url)
        content = soup.select(query)
        return [self._get_attrs(node) for node in content]

    def _get_raw_content(self, url: str, query: str) -> List[Tag]:
        soup = self._request_soup(url)
        return list(soup.select(query))

    def _extract_problem_id(self, url: str, elements: List[Dict[str, str]]) -> str:
        params_url = parse_qs(urlparse(url).query)
        problem_id = params_url.get("id", [None])[0]
        if problem_id:
            return problem_id

        # En algunos enlaces de concurso viene cid/pid sin id directo.
        cid = params_url.get("cid", [None])[0]
        pid = params_url.get("pid", [None])[0]
        if cid and pid:
            return f"{cid}-{pid}"

        for element in elements:
            if element.get("text") == "Estado" and element.get("href"):
                status_url = urljoin(self.base_url, element["href"])
                status_params = parse_qs(urlparse(status_url).query)
                status_id = status_params.get("id", [None])[0]
                if status_id:
                    return status_id

        raise ValueError("No se pudo extraer el id del problema desde la URL.")

    def _extract_problem_title(self, elements: List[Dict[str, str]]) -> str:
        for tag in ("h2", "h3"):
            for element in elements:
                if element.get("name") == tag and element.get("text"):
                    return element["text"]
        raise ValueError("No se pudo extraer el titulo del problema.")

    def _build_elements_text(self, elements: List[Dict[str, str]]) -> List[str]:
        seen = set()
        lines: List[str] = []
        for element in elements:
            text = element.get("text", "")
            tag_name = element.get("name", "")
            if not text:
                continue
            line = f"{' ' * self.indent_by_tag.get(tag_name, 1)} {text}"
            if line in seen:
                continue
            seen.add(line)
            lines.append(line)
        return lines

    def _problem_file_path(self, problem_id: str, title: str) -> str:
        filename = self._sanitize_filename(f"{problem_id}_{title}") + ".py"
        return os.path.join(self.path, filename)

    def _merge_legacy_file(self, problem_id: str, target_file: str):
        legacy_file = os.path.join(self.path, f"{problem_id}.py")
        if not os.path.exists(legacy_file):
            return

        with open(legacy_file, "r", encoding="utf-8") as old_file:
            with open(target_file, "a", encoding="utf-8") as new_file:
                new_file.write(old_file.read())
        os.remove(legacy_file)

    def create_problem(self, url: str) -> Tuple[str, str]:
        elements = self._get_content(url, "main h2, main h3, main a, main span, main p, main pre")
        problem_id = self._extract_problem_id(url, elements)
        title = self._extract_problem_title(elements)
        file_path = self._problem_file_path(problem_id, title)

        if os.path.exists(file_path):
            return "ya_existe", file_path

        params_url = parse_qs(urlparse(url).query)
        elements_text = self._build_elements_text(elements)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"# {url}\n#")
            if not params_url.get("id", [None])[0]:
                file.write(f"# {self.base_url}problem.php?id={problem_id}\n#")
            file.write("\n#".join(elements_text))
            file.write("\n\n")

        self._merge_legacy_file(problem_id, file_path)
        return "creado", file_path

    def _get_from_table(self, url: str) -> List[Dict[str, str]]:
        tables = self._get_raw_content(url, query="main table")
        if not tables:
            raise ValueError("No se encontro una tabla de problemas en el concurso.")

        rows = tables[0].select("tbody tr")
        links = [row.select("td a")[0] for row in rows if row.select("td a")]
        return [self._get_attrs(link) for link in links]

    def create_contest(self, url: str, continue_on_error: bool = True) -> List[Tuple[str, str, str]]:
        results: List[Tuple[str, str, str]] = []
        for row in self._get_from_table(url):
            if "href" not in row:
                continue
            problem_url = urljoin(self.base_url, row["href"])
            try:
                status, file_path = self.create_problem(problem_url)
                results.append((status, file_path, problem_url))
            except Exception:
                results.append(("error", "", problem_url))
                if not continue_on_error:
                    raise
        return results