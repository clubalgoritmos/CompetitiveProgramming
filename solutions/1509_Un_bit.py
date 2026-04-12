# https://jv.umsa.bo/oj/problem.php?id=1509
#  Un bit
#  Enviar
#  Estado
#  Descripción
#    Para este problema te pedimos que imprimas el i-esimo numero natural que en su representación binaria tiene exactamente un bit encendido.
#   Entrada
#    La primera linea viene un numero $t$ $(1 \leq t \leq 60)$ que indica el numero de casos de prueba a procesar.
#    A continuación t lineas, en cada linea un numero $x$ $(1 \leq x \leq 60)$, que indica que debes imprimir el x-esimo numero natural que en su representación binaria tiene exactamente un bit encendido.
#   Salida
#    Por cada numero x, imprimir en una linea(sin espacios adicionales) el x-esimo numero natural que tiene exactamente un solo bit encendido en su representación binaria.
#   Ejemplo Entrada
#    3183
#   Ejemplo Salida
#    11284
#   Ayuda
#    2da div. 2017 UMSA

for _ in range(int(input())):
    N = int(input())
    print(2**(N-1))