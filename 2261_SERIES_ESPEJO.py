# https://jv.umsa.bo/oj/problem.php?id=2261
#  SERIES ESPEJO
#  Enviar
#  Estado
#  Descripción
#    Descifra la siguiente serie:
#    1 -1 2 -2 3 -3 4 -4 5 -5 6 -6 7 -7 8 -8…
#   Entrada
#    Un número n donde 1 <= n <= 1000
#   Salida
#   Ejemplo Entrada
#    3
#   Ejemplo Salida
#    1 -1 2
#   Ayuda
for i in range(int(input())):
    if i%2==0:
        print(int((i+2)/2),end=" ")
        continue
    print(-int((i+2)/2),end=" ")