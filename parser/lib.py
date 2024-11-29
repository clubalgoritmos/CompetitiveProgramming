import requests
import re
import os
import argparse
from bs4 import BeautifulSoup
from urllib.parse import parse_qs, urlparse
import shutil

class Problem:
    def __init__(self, id: str, title: str, url: str, path: str, pid: str = None, elements: list = None):
        if not pid:
            self.id = id
        else:
            self.id = f"{id}-{pid}"
        self.title = title
        self.url = url
        self.path = path
        self.solved = os.path.exists(self.generate_path())
        self.elements = elements

    def __str__(self):
        return f"{self.id} {self.title} {self.url}"

    def generate_path(self):
        return os.path.join(
            self.path,
            re.sub(r'[\\/:*?"<>|]', "", f"{self.id}_{self.title}").replace(" ", "_") + ".py",
        )

    def get(self):
        elements = self._get_content(self.url, "main h2, main h3, main a, main span, main p, main pre")

        def search_send():
            for element in elements:
                if element["text"] == "Estado":
                    return self.base_url + element["href"]
            return self.base_url

    def save(self, path: str):
        if self.solved:
            return "ya resuelto"
        file_path = self.generate_path()

        # Crear el archivo
        with open(file_path, "w", encoding='utf-8') as file:  # Abrir el archivo en modo de escritura
            file.write(f"# {self.url}\n#")
            file.write("\n#".join(self.elements))
            file.write("\n\n")

        exist_legacy = os.path.join(self.path, f"{self.id}.py")
        if os.path.exists(exist_legacy):
            with open(exist_legacy, "r") as legacy_file:
                with open(file_path, "a") as new_file:  # Abrir el archivo en modo de agregar
                    new_file.write(legacy_file.read())
            os.remove(exist_legacy)  # Borrar el archivo de donde se ha copiado

        # Imprimir la ruta del archivo
        return file_path

class Parser:
    def __init__(self, path: str = os.getcwd()):
        self.path = path
        self.valores = {
            "h2": 1,
            "h3": 2,
            "span": 3,
            "p": 3,
            "pre": 3,
            "a": 1
        }
        self.base_url = "https://jv.umsa.bo/oj/"
        pass

    # Función para obtener el texto de un elemento
    def _get_attrs(self, element):
        attrs = element.attrs
        attrs["text"] = "".join(ch for ch in element.get_text().strip() if ch.isprintable())
        attrs["name"] = element.name
        return attrs

    def _get_content(self, url: str, query: str, raw: bool = False):
        # Realizar la solicitud HTTP
        response = requests.get(url)

        # Analizar el HTML con BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        content = soup.select(query)

        if raw:
            return content
        elements = list(map(self._get_attrs, content))
        return elements

    def get_contest(self, url: str):
        title = self._get_content(url, "main h3")[0]["text"]
        table = self._get_from_table(url)
        print(title, url)

        for row in table:
            print(self.create_problem(self.base_url + row["href"]))

    def _get_from_table(self, url: str):
        table = self._get_content(url, query="main table", raw=True)[0]

        # Obtener las filas de la tabla
        rows = table.select("tbody tr")

        # Obtener el texto de las filas
        rows = list(map(lambda row: row.select("td a")[0], rows))
        # Obtener el texto de las filas
        elements = list(map(self._get_attrs, rows))

        return elements

    def create_problem(self, url: str):
        elements = self._get_content(url, "main h2, main h3, main a, main span, main p, main pre")

        def search_send():
            for element in elements:
                if element["text"] == "Estado":
                    return self.base_url + element["href"]
            return self.base_url

        # Parsear la URL para obtener el argumento 'id'
        params_url = parse_qs(urlparse(url).query)
        params_statusurl = parse_qs(urlparse(search_send()).query)
        id = params_url.get("id", [None])[0] or params_statusurl.get("id", [None])[0] or params_url.get("cid", [None])[0] + "-" + params_url.get("pid", [None])[0]

        # Ruta del archivo
        file_path = os.path.join(
            self.path,
            re.sub(r'[\\/:*?"<>|]', "", f"{id}_{elements[1]['text']}").replace(" ", "_") + ".py",
        )

        # Verificar si el archivo ya existe
        if os.path.exists(file_path):
            return "ya resuelto", file_path

        seen = set()
        elements_text = [f"{' ' * self.valores[el['name']]} {el['text']}" for el in elements if el['text'] != "" and f"{' ' * self.valores[el['name']]} {el['text']}" not in seen and not seen.add(f"{' ' * self.valores[el['name']]} {el['text']}")]

        # Crear el archivo
        with open(file_path, "w", encoding='utf-8') as file:  # Abrir el archivo en modo de escritura
            file.write(f"# {url}\n#")
            if not params_url.get("id", [None])[0]:
                file.write(f"# {self.base_url}problem.php?id={id}\n#")
            file.write("\n#".join(elements_text))
            file.write("\n\n")

        exist_legacy = os.path.join(self.path, f"{id}.py")
        if os.path.exists(exist_legacy):
            with open(exist_legacy, "r") as legacy_file:
                with open(file_path, "a") as new_file:  # Abrir el archivo en modo de agregar
                    new_file.write(legacy_file.read())
            os.remove(exist_legacy)  # Borrar el archivo de donde se ha copiado

        # Imprimir la ruta del archivo
        return file_path

def main():
    parser = argparse.ArgumentParser(description="Herramienta para crear problemas desde una URL")
    parser.add_argument("url", type=str, help="URL del problema o concurso")
    parser.add_argument("--path", type=str, default=os.getcwd(), help="Ruta donde se guardarán los problemas")
    parser.add_argument("--contest", action="store_true", help="Indica si la URL es de un concurso")

    args = parser.parse_args()

    parser_obj = Parser(path=args.path)

    if args.contest:
        parser_obj.get_contest(args.url)
    else:
        print(parser_obj.create_problem(args.url))

if __name__ == "__main__":
    main()