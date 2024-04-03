# https://jv.umsa.bo/oj/problem.php?cid=2818&pid=11
## https://jv.umsa.bo/oj/problem.php?id=2072
#  Más Menos
#  Enviar
#  Estado
#  Descripción
#    Alexis es un buen muchacho que le gustan las matematicas, realizo la suma y resta de dos numeros $A$ y $B$.
#    $A + B = X$
#    $A − B = Y$
#    Ahora Alexis te reta a adivinar los numeros que sumo y resto, el te dara los resultados $X$ e $Y$, tu tarea es hallar $A$ y $B$, para ganar el reto de Alexis.
#   Entrada
#    La entrada consiste de $N$ casos de prueba, por cada caso de prueba se te dara $X$ e $Y$ , $(1 ≤ X, Y ≤ 10^9 )$
#   Salida
#    Por cada caso de prueba imprima $A$ y $B$.
#   Ejemplo Entrada
#    25 95 5
#   Ejemplo Salida
#    7 -25 0
#   Ayuda
#    En la salida A tiene que ser mayor igual a B.

t = int(input())
for _ in range(t):
    X, Y = map(int,input().split())
    # A + B = X
    # A - B = Y
    # 2A = X + Y
    # A = (X + Y) // 2
    A = (X + Y) // 2
    # A + B = X
    # B = X - A
    B = X - A
    print(A,B)