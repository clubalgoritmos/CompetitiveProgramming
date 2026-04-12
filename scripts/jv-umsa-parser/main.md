## jv-umsa-parser

CLI para generar archivos `.py` base desde problemas de [jv.umsa.bo](https://jv.umsa.bo/oj/).

### 1) Instalacion

```bash
pip install -r requirements.txt
```

### 2) Uso rapido

```bash
python main.py problem "https://jv.umsa.bo/oj/problem.php?id=1000"
```

### 3) Comandos

1. Crear un problema:

```bash
python main.py problem "URL_DEL_PROBLEMA"
```

2. Crear todos los problemas de un concurso:

```bash
python main.py contest "URL_DEL_CONCURSO"
```

3. Definir carpeta de salida personalizada:

```bash
python main.py -p "RUTA_DE_SALIDA" problem "URL_DEL_PROBLEMA"
```

4. Cambiar timeout de red:

```bash
python main.py --timeout 30 problem "URL_DEL_PROBLEMA"
```

5. Detener en el primer error durante concurso:

```bash
python main.py contest "URL_DEL_CONCURSO" --fail-fast
```

### 4) Ayuda

```bash
python main.py --help
python main.py problem --help
python main.py contest --help
```