# https://jv.umsa.bo/oj/problem.php?cid=2823&pid=2
## https://jv.umsa.bo/oj/problem.php?id=2440
#  Sumatoria de la Progresión Aritmética 1
#  Enviar
#  Estado
#  Descripción
#    Hallar el resultado de la siguiente sumatoria para n términos: S = 30 + 20 + 10 + 0 – 10 - 20 - ...
#   Entrada
#    Contiene un número n (1 ≤ n ≤ 500)
#   Salida
#    Imprima en una línea el valor correspondiente a la suma de los n primeros términos de la progresión aritmética.
#   Ejemplo Entrada
#    3
#   Ejemplo Salida
#    60
#   Ayuda

N = int(input())
print(N*(30 - 10*(N-1)//2))