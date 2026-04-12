# https://jv.umsa.bo/oj/problem.php?cid=2823&pid=3
## https://jv.umsa.bo/oj/problem.php?id=2441
#  Sumatoria de la Progresión Geométrica 1
#  Enviar
#  Estado
#  Descripción
#    Hallar el resultado de la siguiente sumatoria para n términos: S = 16 + 12 + 9 + 27/4 + 81/16 + ...
#   Entrada
#    Contiene un número n (1 ≤ n ≤ 50)
#   Salida
#    Imprima en una línea el valor correspondiente a la suma de los n primeros términos de la progresión geométrica.Este número deberá ser mostrado con 4 decimales de precisión.
#   Ejemplo Entrada
#    3
#   Ejemplo Salida
#    37.0000
#   Ayuda
x = 16
S = 0
N = int(input())
for _ in range(N):
    S += x
    x *= 3/4
print("{:.4f}".format(S))