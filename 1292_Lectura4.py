# https://jv.umsa.bo/oj/problem.php?id=1292
#  Lectura4
#  Enviar
#  Estado
#  Descripción
#    Verificar el fin de archivo preguntando si n es cero
#   Entrada
#   Salida
#    Por cada caso de prueba escrita en una linea la suma de los números.
#   Ejemplo Entrada
#    41 2 3 4109 8 7 6 5 4 3 2 1 -55-1 -3 5 3 10
#   Ejemplo Salida
#    10405
#   Ayuda

while True:
    try:
        n=int(input())
        print(sum(map(int, input().split())))
    except EOFError:
        break