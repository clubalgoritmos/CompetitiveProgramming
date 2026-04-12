import os
import re
import yaml
from pathlib import Path
from collections import defaultdict

def parse_metadata(file_path):
    metadata = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Buscar lineas como #| key: value o //| key: value
    pattern = re.compile(r'^[#\/]+\|\s*(\w+):\s*(.*)$', re.MULTILINE)
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

def main():
    solutions_dir = Path('solutions')
    docs_dir = Path('docs')
    output_dir = docs_dir / 'problems'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Estructura: problems[competition][problem_id] = list of files
    problems = defaultdict(lambda: defaultdict(list))
    
    # Recolectar metadatos
    for ext in ['*.py', '*.cpp']:
        for file_path in solutions_dir.glob(ext):
            meta = parse_metadata(file_path)
            if 'competition' in meta and 'problem_id' in meta:
                meta['file_path'] = str(file_path)
                meta['ext'] = ext.replace('*', '')
                problems[meta['competition']][meta['problem_id']].append(meta)

    # Generar archivos QMD
    for competition, probs in problems.items():
        comp_dir = output_dir / competition.replace(' ', '_')
        comp_dir.mkdir(parents=True, exist_ok=True)
        
        for problem_id, files in probs.items():
            first_meta = files[0]
            title = first_meta.get('title', f"Problem {problem_id}")
            tags = first_meta.get('tags', [])
            desc = first_meta.get('description', '')
            
            qmd_path = comp_dir / f"{problem_id}.qmd"
            with open(qmd_path, 'w', encoding='utf-8') as f:
                f.write("---\n")
                f.write(f"title: \"Problema {problem_id}: {title}\"\n")
                if tags:
                    f.write(f"categories: {tags}\n")
                f.write("---\n\n")
                
                if desc:
                    f.write(f"{desc}\n\n")
                    
                f.write("::: {.panel-tabset}\n\n")
                
                for meta in files:
                    lang = meta.get('language', 'Code')
                    approach = meta.get('approach', 'Solución')
                    f.write(f"### {lang} ({approach})\n")
                    
                    code_lang = 'python' if meta['ext'] == '.py' else 'cpp'
                    f.write(f"```{{python}} # Cambiar a cpp si corresponde (ej usando un modulo intermedio)\n")
                    f.write(f"{{{{< include ../../../{meta['file_path']} >}}}}\n")
                    f.write(f"```\n\n")
                    
                f.write(":::\n")
                
    print(f"Sitio construido exitosamente en {output_dir}")

if __name__ == '__main__':
    main()
