# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=234
## https://jv.umsa.bo/oj/problem.php?id=2649
#    Copiado al portapapeles
#  Ordenando 4 números
#  Enviar
#  Estado
#  Descripción
#    Dado cuatro números a, b, c, d, ordenar en forma ascendente, solo utilizando condicionales.
#   Entrada
#    La entrada consiste en múltiples casos de prueba, cada caso viene dado en una línea con 4 números enteros -10000 <= a, b, c, d <= 10000
#   Salida
#    La salida consiste para cada caso en los 4 números ordenados de forma ascendente.
#   Ejemplo Entrada
#    2 1 7 65 0 3 0
#   Ejemplo Salida
#    1 2 6 70 0 3 5
#   Ayuda

while True:
    try:
        a = sorted(map(int, input().split()))
        print(*a)
    except EOFError:
        break
