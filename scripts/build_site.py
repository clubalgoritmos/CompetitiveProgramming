import re
import json
import os
from pathlib import Path
from collections import defaultdict

def parse_metadata(file_path):
    metadata = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Buscar lineas como #| key: value, # | key: value, //| key: value o // | key: value
    pattern = re.compile(r'^\s*(?:#|//)\s*\|\s*([A-Za-z_][\w-]*)\s*:\s*(.*)$', re.MULTILINE)
    for match in pattern.finditer(content):
        key = match.group(1)
        value = match.group(2).strip(' "\'')
        if value.startswith('[') and value.endswith(']'):
            # Simple list parsing
            items = [item.strip(' "\'') for item in value[1:-1].split(',')]
            metadata[key] = items
        else:
            metadata[key] = value
            
    return metadata


def slugify(value):
    slug = re.sub(r"[^A-Za-z0-9]+", "_", value.strip())
    slug = slug.strip("_")
    return slug or "item"

def main():
    solutions_dir = Path('solutions')
    docs_dir = Path('docs')
    output_dir = docs_dir / 'problems'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Estructura: problems[competition][problem_id] = list of files
    problems = defaultdict(lambda: defaultdict(list))
    
    processed_count = 0
    skipped_count = 0

    # Recolectar metadatos
    for ext in ['*.py', '*.cpp']:
        for file_path in solutions_dir.rglob(ext):
            meta = parse_metadata(file_path)
            if 'competition' in meta and 'problem_id' in meta:
                meta['file_path'] = str(file_path)
                meta['ext'] = ext.replace('*', '')
                problems[meta['competition']][meta['problem_id']].append(meta)
                processed_count += 1
            else:
                skipped_count += 1
                
    if processed_count == 0:
        print(f"No se encontraron soluciones con metadatos. Se omitieron {skipped_count} archivos.")
        print("Recuerda agregar bloques '#| competition: ...' y '#| problem_id: ...' a tus scripts.")
        return

    catalog = []

    # Generar archivos QMD
    for competition, probs in problems.items():
        comp_slug = slugify(competition)
        comp_dir = output_dir / comp_slug
        comp_dir.mkdir(parents=True, exist_ok=True)
        
        for problem_id, files in probs.items():
            files = sorted(files, key=lambda item: (item.get('language', ''), item.get('file_path', '')))
            first_meta = files[0]
            title = first_meta.get('title', f"Problem {problem_id}")
            desc = first_meta.get('description', '')
            problem_slug = slugify(problem_id)
            tag_set = []
            for meta in files:
                for tag in meta.get('tags', []):
                    if tag and tag not in tag_set:
                        tag_set.append(tag)
            languages = []
            for meta in files:
                lang = meta.get('language', 'Code')
                if lang not in languages:
                    languages.append(lang)
            
            qmd_path = comp_dir / f"{problem_slug}.qmd"
            with open(qmd_path, 'w', encoding='utf-8') as f:
                f.write("---\n")
                f.write(f"title: \"Problema {problem_id}: {title}\"\n")
                if tag_set:
                    f.write("categories:\n")
                    for tag in tag_set:
                        f.write(f"  - \"{tag}\"\n")
                f.write("---\n\n")
                
                if desc:
                    f.write(f"{desc}\n\n")
                    
                f.write("::: {.panel-tabset}\n\n")
                
                for meta in files:
                    lang = meta.get('language', 'Code')
                    approach = meta.get('approach', 'Solución')
                    f.write(f"### {lang} ({approach})\n")
                    
                    code_lang = 'python' if meta['ext'] == '.py' else 'cpp'
                    include_path = Path(meta['file_path'])
                    rel_include = os.path.relpath(include_path, start=qmd_path.parent)
                    rel_include = Path(rel_include).as_posix()
                    f.write(f"```{code_lang}\n")
                    f.write(f"{{{{< include \"{rel_include}\" >}}}}\n")
                    f.write(f"```\n\n")
                    
                f.write(":::\n")

            catalog.append({
                "competition": competition,
                "competition_slug": comp_slug,
                "problem_id": problem_id,
                "problem_slug": problem_slug,
                "title": title,
                "description": desc,
                "tags": tag_set,
                "languages": languages,
                "solutions_count": len(files),
                "url": f"problems/{comp_slug}/{problem_slug}.html",
            })

    catalog = sorted(catalog, key=lambda item: (item["competition"].lower(), str(item["problem_id"]).lower()))
    catalog_path = output_dir / 'catalog.json'
    with open(catalog_path, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
                
    print(f"Sitio construido exitosamente en {output_dir}")
    print(f"Problemas generados: {len(catalog)} | Archivos omitidos por falta de metadatos: {skipped_count}")

if __name__ == '__main__':
    main()
