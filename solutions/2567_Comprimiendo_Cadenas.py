# https://jv.umsa.bo/oj/problem.php?id=2567
#  Comprimiendo Cadenas
#  Enviar
#  Estado
#  Descripción
#    Dada una cadena que contiene una secuencia de caracteres alfabéticos y que representa a un código, se pide comprimir la cadena escribiendo cada letra o carácter una sola vez y también mostrar la cantidad de caracteres que fueron eliminados al lado de cada carácter impreso, tal como se muestra en el ejemplo.
#    Dada una cadena que contiene una secuencia de caracteres alfabéticos y que representa a un código, se pide comprimir la cadena escribiendo cada letra o carácter una sola vez y también mostrar la cantidad de caracteres que fueron eliminados al lado de cada carácter impreso, tal como se muestra en el ejemplo.
#    Dada una cadena que contiene una secuencia de caracteres alfabéticos y que representa a un código, se pide comprimir la cadena escribiendo cada letra o carácter una sola vez y también mostrar la cantidad de caracteres que fueron eliminados al lado de cada carácter impreso, tal como se muestra en el ejemplo.
#   Entrada
#    una simple cadena de caracteres.
#    una simple cadena de caracteres.
#   Salida
#    Una única cadena sin espacios al final ni al principio.
#    Una única cadena sin espacios al final ni al principio.
#   Ejemplo Entrada
#    BBBBUUUENNNNNAA----SSSSUEEERRTTTE
#   Ejemplo Salida
#    B3U2E0N4A1-3S3U0E2R1T2E0
#   Ayuda

V = [x for x in input()]
aux = V[0]
B = aux
c = 0
for i in range(1, len(V)):
  if V[i] == aux:
    c = c+1
  else:
    aux = V[i]
    B = f"{B}{c}{aux}"
    c = 0
B = f"{B}{c}"
print(B)