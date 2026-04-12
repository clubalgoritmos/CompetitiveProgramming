Para implementar este proyecto con la estructura de navegación **Competencias > Problemas > Soluciones** y asegurar que sea escalable para múltiples lenguajes y lógicas, he diseñado el siguiente plan de implementación técnica.

Este plan se basa en tu filosofía de "hacer una cosa que sirva para muchas", automatizando el paso de scripts puros a una plataforma interactiva.

---

### Fase 1: Estandarización de Metadatos (El "Contrato")
Para que el sistema sea automático, cada script (`.py`, `.cpp`) debe actuar como su propia base de datos mediante comentarios estructurados en la cabecera.

**Propuesta de Formato:**
```python
#| competition: "ICPC Bolivia Pre-National 2024"
#| problem_id: "A"
#| title: "Areas"
#| tags: [Geometry, Math]
#| language: "Python"
#| approach: "Integral de línea"
#| description: "Cálculo de áreas irregulares mediante descomposición..."
#| link: "https://jv.umsa.bo/problem.php?id=..."
```

---

### Fase 2: Arquitectura de Navegación (Quarto Structure)
La navegación se gestionará a través del archivo `_quarto.yml` para reflejar la jerarquía solicitada.

**Estructura del sitio:**
1.  **Nivel 1 (Competencias):** Una página índice con un `listing` de tipo `grid` que agrupe carpetas (ej. 2024-Bolivia, 2023-Regional).
2.  **Nivel 2 (Problemas):** Dentro de cada competencia, un `listing` de tipo `table` que muestre los problemas resueltos, sus tags y dificultad.
3.  **Nivel 3 (Soluciones):** La página final del problema que agrupará todos los scripts asociados.

---

### Fase 3: El Script "Generador de Conocimiento"
Desarrollarás un script en Python (`build_site.py`) que automatice la creación de los archivos `.qmd` para no tener que escribirlos a mano.

**Lógica del Generador:**
1.  **Escaneo:** Recorre recursivamente tu repositorio unificado.
2.  **Agrupación:** Agrupa archivos que tengan el mismo `problem_id` dentro de la misma `competition`.
3.  **Generación de `.qmd`:** Crea un archivo por problema que use **Tabsets** de Quarto para mostrar las diferentes soluciones.

**Ejemplo de salida automática (`problema_A.qmd`):**
```markdown
---
title: "Problema A: Areas"
categories: [Geometry, Math]
---
{{< include _descripcion_extraida.md >}}

::: {.panel-tabset}
### Python (Lógica 1)
{{< include solutions/A_Areas.py >}}

### C++ (Optimizado)
{{< include solutions/A_Areas.cpp >}}
:::
```

---

### Fase 4: Implementación de WebAssembly (Interactividad)
Para la ejecución en el navegador sin servidores, integraremos motores de Wasm:

* **Python:** Utilizar la extensión `quarto-live` (basada en **Pyodide**). Esto transformará tus bloques de código `python` en editores interactivos donde el usuario podrá ejecutar `input()` y ver el `output` real.
* **C++:** Dado que C++ requiere compilación, la estrategia inicial será usar un componente de **Monaco Editor** vinculado a un motor de ejecución Wasm (como `clang-wasm`) o, en una fase inicial, un enlace directo a un entorno de ejecución seguro.

---

### Fase 5: Automatización y Despliegue (CI/CD)
Para que solo tengas que hacer `git push`, configuraremos un **GitHub Action**:

1.  **Trigger:** Se activa al detectar cambios en la rama `main`.
2.  **Build:**
    * Ejecuta `build_site.py` para generar los archivos `.qmd`.
    * Ejecuta `quarto render` para generar el sitio HTML estático.
3.  **Deploy:** Publica el resultado en **Cloudflare Pages**.

---

### Checklist de Inicio
* [ ] Realizar el merge final de todas las ramas a `main`.
* [ ] Crear el archivo `_quarto.yml` con la configuración de navegación.
* [ ] Añadir metadatos al menos a 3 problemas para probar el script generador.
* [ ] Configurar el primer `listing` en la página principal para visualizar las competencias.

Este plan transforma tu repositorio de una carpeta de archivos en una **base de conocimiento técnica** que demuestra tu capacidad de automatización y diseño de sistemas. ¿Te gustaría que escribamos el código base para el `build_site.py`?