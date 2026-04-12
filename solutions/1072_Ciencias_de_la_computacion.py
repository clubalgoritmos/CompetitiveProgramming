# https://jv.umsa.bo/problem.php?id=1072
#  Ciencias de la computacion
#  Enviar
#  Estado
#  Descripción
#    Botas estudia Ciencias de la Computacion y le quedan por cursar n materias. El sabe que si hace una sola materia le va a costar 1 unidad de esfuerzo aprobarla, pero si hace una segunda materia le cuesta 2 unidades de esfuerzo para aprobar la segunda materia, y en general, si hace i materias le cuesta i unidades de esfuerzo aprobar la i-esima materia. El sabe que hacer un esfuerzo de E unidades o mas lo va a estrezar y por lo tanto va a dejar la carrera. Cuantas materias como maximo puede tomar por semestre?
#   Entrada
#    La entrada esta compuesta por un numero $T$ ($1 \leq T \leq 10^5$) el numero de casos de prueba, seguido por $T$ lineas compuestas por dos numeros $N$ y $E$ ($1 \leq N \leq 4 * 10000$) ($1 \leq E \leq 1000000000$), el numero de materias y esfuerzo maximo respectivamente.
#   Salida
#    Por cada caso de prueba imprimir una linea que contiene el numero maximo de materias que puede tomar en un semestre.
#   Ejemplo Entrada
#    210 1010 11
#   Ejemplo Salida
#    34
#   Ayuda

import math
for _ in range(int(input())):
    n, k = map(int, input().split())
    if k == 0:
        m = 0
    else:
        m = int((-1 + math.sqrt(1 + 8 * (k - 1))) // 2)
    print(min(m, n))