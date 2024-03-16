import re

# Abre el archivo y lee el contenido
with open('C:\\Users\\Andres\\Proyectos\\PyCompetitiveProgramming\\parser\\text.txt', 'r') as f:
    content = f.read()

# Encuentra todos los textos que contienen exactamente 4 dígitos rodeados por espacios (o al principio o al final del texto)
matches = re.findall(r'(?:^|\s)(\d{4})(?:\s|$)', content)

# Imprime solo los números de 4 dígitos
for match in matches:
    print(match)