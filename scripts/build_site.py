import re
import json
import os
from pathlib import Path
from collections import defaultdict


def parse_metadata(file_path):
    metadata = {}
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Buscar lineas como #| key: value, # | key: value, //| key: value o // | key: value
    pattern = re.compile(r"^\s*(?:#|//)\s*\|\s*([A-Za-z_][\w-]*)\s*:\s*(.*)$", re.MULTILINE)
    for match in pattern.finditer(content):
        key = match.group(1)
        value = match.group(2).strip(" \"'")
        if value.startswith("[") and value.endswith("]"):
            # Simple list parsing
            items = [item.strip(" \"'") for item in value[1:-1].split(",")]
            metadata[key] = items
        else:
            metadata[key] = value

    return metadata


def slugify(value):
    slug = re.sub(r"[^A-Za-z0-9]+", "_", value.strip())
    slug = slug.strip("_")
    return slug or "item"


def yaml_quote(value):
    text = str(value)
    text = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def rewrite_markdown_links(content, readme_path, repo_blob_base):
    readme_parent = readme_path.parent

    def replace(match):
        label = match.group(1)
        target = match.group(2).strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)

        absolute_target = (readme_parent / target).resolve()
        project_root = Path.cwd().resolve()
        try:
            rel_target = absolute_target.relative_to(project_root)
            github_url = f"{repo_blob_base}/{rel_target.as_posix()}"
            return f"[{label}]({github_url})"
        except ValueError:
            return match.group(0)

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace, content)


def main():
    repo_blob_base = "https://github.com/clubalgoritmos/CompetitiveProgramming/blob/main"
    solutions_dir = Path("solutions")
    docs_dir = Path("docs")
    output_dir = docs_dir / "problems"
    competitions_dir = docs_dir / "competitions"
    output_dir.mkdir(parents=True, exist_ok=True)
    competitions_dir.mkdir(parents=True, exist_ok=True)

    # Estructura: problems[competition][problem_id] = list of files
    problems = defaultdict(lambda: defaultdict(list))

    processed_count = 0
    skipped_count = 0

    # Recolectar metadatos
    for ext in ["*.py", "*.cpp"]:
        for file_path in solutions_dir.rglob(ext):
            meta = parse_metadata(file_path)
            if "competition" in meta and "problem_id" in meta:
                meta["file_path"] = str(file_path)
                meta["ext"] = ext.replace("*", "")
                problems[meta["competition"]][meta["problem_id"]].append(meta)
                processed_count += 1
            else:
                skipped_count += 1

    if processed_count == 0:
        print(f"No se encontraron soluciones con metadatos. Se omitieron {skipped_count} archivos.")
        print(
            "Recuerda agregar bloques '#| competition: ...' y '#| problem_id: ...' a tus scripts."
        )
        return

    catalog = []

    # Generar archivos QMD
    for competition, probs in problems.items():
        comp_slug = slugify(competition)
        comp_dir = output_dir / comp_slug
        comp_dir.mkdir(parents=True, exist_ok=True)
        competition_tags = []
        competition_readme = None

        for problem_id, files in probs.items():
            files = sorted(
                files, key=lambda item: (item.get("language", ""), item.get("file_path", ""))
            )
            first_meta = files[0]
            title = first_meta.get("title", f"Problem {problem_id}")
            desc = first_meta.get("description", "")
            official_link = first_meta.get("link", "")
            problem_slug = slugify(problem_id)
            tag_set = []
            for meta in files:
                for tag in meta.get("tags", []):
                    if tag and tag not in tag_set:
                        tag_set.append(tag)
                    if tag and tag not in competition_tags:
                        competition_tags.append(tag)
                path_obj = Path(meta["file_path"])
                readme_candidate = path_obj.parent / "README.md"
                if readme_candidate.exists() and competition_readme is None:
                    competition_readme = readme_candidate
            languages = []
            for meta in files:
                lang = meta.get("language", "Code")
                if lang not in languages:
                    languages.append(lang)
            featured = any(
                str(meta.get("featured", "")).strip().lower() in {"true", "1", "yes", "y"}
                for meta in files
            )

            qmd_path = comp_dir / f"{problem_slug}.qmd"
            with open(qmd_path, "w", encoding="utf-8") as f:
                f.write("---\n")
                f.write(f"title: {yaml_quote(f'Problema {problem_id}: {title}')}\n")
                f.write(f"problem_id: {yaml_quote(problem_id)}\n")
                f.write(f"competition: {yaml_quote(competition)}\n")
                f.write(f"languages: {yaml_quote(', '.join(languages))}\n")
                f.write(f"solutions_count: {len(files)}\n")
                if desc:
                    f.write(f"description: {yaml_quote(desc)}\n")
                if official_link:
                    f.write(f"official_link: {yaml_quote(official_link)}\n")
                f.write(f"featured: {str(featured).lower()}\n")
                if tag_set:
                    f.write("categories:\n")
                    for tag in tag_set:
                        f.write(f"  - {yaml_quote(tag)}\n")
                f.write("---\n\n")

                if desc:
                    f.write(f"{desc}\n\n")

                f.write("::: {.panel-tabset}\n\n")

                for meta in files:
                    lang = meta.get("language", "Code")
                    approach = meta.get("approach", "Solución")
                    f.write(f"### {lang} ({approach})\n")

                    code_lang = "python" if meta["ext"] == ".py" else "cpp"
                    include_path = Path(meta["file_path"])
                    rel_include = os.path.relpath(include_path, start=qmd_path.parent)
                    rel_include = Path(rel_include).as_posix()
                    f.write(f"```{code_lang}\n")
                    f.write(f'{{{{< include "{rel_include}" >}}}}\n')
                    f.write(f"```\n\n")

                f.write(":::\n")

            catalog.append(
                {
                    "competition": competition,
                    "competition_slug": comp_slug,
                    "problem_id": problem_id,
                    "problem_slug": problem_slug,
                    "title": title,
                    "description": desc,
                    "tags": tag_set,
                    "languages": languages,
                    "featured": featured,
                    "solutions_count": len(files),
                    "official_link": official_link,
                    "url": f"problems/{comp_slug}/{problem_slug}.html",
                }
            )

        competition_page = competitions_dir / f"{comp_slug}.qmd"
        with open(competition_page, "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(f"title: {yaml_quote(competition)}\n")
            if competition_tags:
                f.write("categories:\n")
                for tag in competition_tags:
                    f.write(f"  - {yaml_quote(tag)}\n")
            f.write("listing:\n")
            f.write(f"  contents: ../problems/{comp_slug}/*.qmd\n")
            f.write("  type: table\n")
            f.write("  fields: [problem_id, title, categories, languages, solutions_count]\n")
            f.write("  filter-ui: true\n")
            f.write('  sort: "title"\n')
            f.write("  page-size: 20\n")
            f.write("---\n\n")
            if competition_readme is not None:
                readme_text = competition_readme.read_text(encoding="utf-8")
                readme_text = rewrite_markdown_links(
                    readme_text, competition_readme, repo_blob_base
                )
                f.write("## Contexto de la competencia\n\n")
                f.write(readme_text)
                f.write("\n\n")
            f.write("## Problemas\n\n")
            f.write("Problemas de esta competencia.\n")

    catalog = sorted(
        catalog, key=lambda item: (item["competition"].lower(), str(item["problem_id"]).lower())
    )
    catalog_path = output_dir / "catalog.json"
    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

    print(f"Sitio construido exitosamente en {output_dir}")
    print(
        f"Problemas generados: {len(catalog)} | Archivos omitidos por falta de metadatos: {skipped_count}"
    )


if __name__ == "__main__":
    main()
