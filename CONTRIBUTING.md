# Guía de Contribución

¡Gracias por tu interés en contribuir a este repositorio de Programación Competitiva! Este proyecto está diseñado para funcionar como una base de conocimiento interactiva y automatizada.

Para mantener el orden y asegurar que el generador de la documentación funcione correctamente, te pedimos que sigas estas directrices al agregar nuevas soluciones.

## 1. Agregar Nuevas Soluciones

Todas las soluciones deben ubicarse dentro de la carpeta `solutions/`. Puedes nombrar tu archivo de forma descriptiva, pero lo más importante es incluir los **metadatos** en la cabecera del archivo. 

El script generador (`scripts/build_site.py`) lee estos metadatos para construir automáticamente el sitio web, agrupar las soluciones por problema y competencia, y mostrarlas en pestañas.

### Formato de Metadatos

Los metadatos constan de comentarios especiales al inicio de tu script. Usa `#|` para Python y `//|` para C++.

**Ejemplo para Python (`.py`):**
```python
#| competition: "ICPC Bolivia Pre-National 2024"
#| problem_id: "A"
#| title: "Nombre del Problema"
#| tags: [Matemáticas, Grafos]
#| language: "Python"
#| approach: "Solución Inicial (Fuerza Bruta)"
#| description: "Breve descripción de la lógica utilizada."

def solve():
    pass
```

**Ejemplo para C++ (`.cpp`):**
```cpp
//| competition: "ICPC Bolivia Pre-National 2024"
//| problem_id: "A"
//| title: "Nombre del Problema"
//| tags: [Matemáticas, Programación Dinámica]
//| language: "C++"
//| approach: "Solución Optimizada O(N log N)"
//| description: "Uso de Segment Trees para optimizar las consultas."

#include <iostream>
using namespace std;

int main() {
    return 0;
}
```

### Campos Obligatorios
* `competition`: Nombre de la competencia, plataforma o juez (ej. *LeetCode*, *Codeforces Round 800*, *UMSA*).
* `problem_id`: Identificador único del problema en esa competencia (ej. `A`, `1000`, `TwoSum`).
* `title`: Título legible del problema.

### Campos Recomendados
* `language`: Lenguaje utilizado (Python, C++, Java, etc.).
* `approach`: Descripción corta de la técnica o complejidad temporal.
* `tags`: Lista con corchetes de los temas repasados.
* `description`: Explicación concisa para guiar al lector en tu código.

## 2. Generar la Documentación

Una vez que hayas agregado o modificado un script en `solutions/`, debes ejecutar el script generador de páginas integrado. Esto convertirá tus archivos de código en páginas `.qmd` (Quarto) interactivas.

```bash
# Ejecutar desde la raíz del proyecto
python scripts/build_site.py
```

## 3. Previsualizar los Cambios

Para asegurarte de que tus contribuciones se ven correctamente en la web antes de enviar tus cambios (Pull Request), necesitas tener [Quarto](https://quarto.org/docs/get-started/) instalado.

Ejecuta el siguiente comando para abrir una vista previa en vivo en tu navegador:

```bash
quarto preview
```

Si todo luce bien, ¡haz un *commit* con tus cambios y abre un *Pull Request*!
