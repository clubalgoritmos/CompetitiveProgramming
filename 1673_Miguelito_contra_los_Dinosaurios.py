# https://jv.umsa.bo/oj/problem.php?id=1673
#  Miguelito contra los Dinosaurios
#  Enviar
#  Estado
#  Descripción
#    En la Escuela de poderes ACM Miguelito fue a luchar contra su Centro de Estudiantes, por su falta de seriedad a la hora de repartir galletas (es un problema muy serio en los centros de estudiantes de todo el mundo).
#    En la Escuela de poderes ACM Miguelito fue a luchar contra su Centro de Estudiantes, por su falta de seriedad a la hora de repartir galletas (es un problema muy serio en los centros de estudiantes de todo el mundo).
#    En la Escuela de poderes ACM Miguelito fue a luchar contra su Centro de Estudiantes, por su falta de seriedad a la hora de repartir galletas (es un problema muy serio en los centros de estudiantes de todo el mundo).
#    Existían $N$ dinosaurios cada uno con varios poderes. Habrá $Q$ rondas para luchar y en cada ronda se variará el poder de Miguelito
#    Existían $N$ dinosaurios cada uno con varios poderes. Habrá $Q$ rondas para luchar y en cada ronda se variará el poder de Miguelito
#    Existían $N$ dinosaurios cada uno con varios poderes. Habrá $Q$ rondas para luchar y en cada ronda se variará el poder de Miguelito
#    Con el poder Miguelito puede hacer dormir a todos los dinosaurios cuyo poder sea menor o igual a $M$ ($\leq M$). Después de cada ronda, despertaran todos los dinosaurios que estén durmiendo en la ronda anterior.
#    Con el poder Miguelito puede hacer dormir a todos los dinosaurios cuyo poder sea menor o igual a $M$ ($\leq M$). Después de cada ronda, despertaran todos los dinosaurios que estén durmiendo en la ronda anterior.
#    Con el poder Miguelito puede hacer dormir a todos los dinosaurios cuyo poder sea menor o igual a $M$ ($\leq M$). Después de cada ronda, despertaran todos los dinosaurios que estén durmiendo en la ronda anterior.
#    Tal que en cada ronda habrá $N$ dinosaurios dispuestos para luchar. Como Miguelito es débil en matemáticas, ayúdalo a contar la cantidad de dinosaurios que puede hacer dormir en cada ronda y la suma total de sus poderes.
#    Tal que en cada ronda habrá $N$ dinosaurios dispuestos para luchar. Como Miguelito es débil en matemáticas, ayúdalo a contar la cantidad de dinosaurios que puede hacer dormir en cada ronda y la suma total de sus poderes.
#    Tal que en cada ronda habrá $N$ dinosaurios dispuestos para luchar. Como Miguelito es débil en matemáticas, ayúdalo a contar la cantidad de dinosaurios que puede hacer dormir en cada ronda y la suma total de sus poderes.
#    Definición de Dinosaurio:
#    Definición de Dinosaurio:
#    Definición de Dinosaurio:
#    Persona que se niega a graduarse de la escuela de poderes ACM
#    Persona que se niega a graduarse de la escuela de poderes ACM
#    Persona que se niega a graduarse de la escuela de poderes ACM
#   Entrada
#    La entrada consiste en un número $N$ ($1 \leq N \leq 10000$), donde es el número de dinosaurios con los que tiene que combatir Miguelito, seguido de $N$ enteros, donde el i-esimo numero son los poderes de cada dinosaurio. ($1 \leq poder-de-cada-dinosaurio \leq 100$)
#    La entrada consiste en un número $N$ ($1 \leq N \leq 10000$), donde es el número de dinosaurios con los que tiene que combatir Miguelito, seguido de $N$ enteros, donde el i-esimo numero son los poderes de cada dinosaurio. ($1 \leq poder-de-cada-dinosaurio \leq 100$)
#    La entrada consiste en un número $N$ ($1 \leq N \leq 10000$), donde es el número de dinosaurios con los que tiene que combatir Miguelito, seguido de $N$ enteros, donde el i-esimo numero son los poderes de cada dinosaurio. ($1 \leq poder-de-cada-dinosaurio \leq 100$)
#    Un numero $Q$($1 \leq Q \leq 10000$)que es el número de rondas que se van a realizar, seguidos de $Q$ enteros que representan el nivel de poder que tendrá Miguelito en esa ronda.($1 \leq potencia-de-Miguelito \leq 100$)
#    Un numero $Q$($1 \leq Q \leq 10000$)que es el número de rondas que se van a realizar, seguidos de $Q$ enteros que representan el nivel de poder que tendrá Miguelito en esa ronda.($1 \leq potencia-de-Miguelito \leq 100$)
#    Un numero $Q$($1 \leq Q \leq 10000$)que es el número de rondas que se van a realizar, seguidos de $Q$ enteros que representan el nivel de poder que tendrá Miguelito en esa ronda.($1 \leq potencia-de-Miguelito \leq 100$)
#   Salida
#    Para cada ronda imprima dos enteros, separados por un espacio
#    Para cada ronda imprima dos enteros, separados por un espacio
#    Para cada ronda imprima dos enteros, separados por un espacio
#    Donde:
#    Donde:
#    Donde:
#    El primer número es la cantidad de dinosaurios
#    El primer número es la cantidad de dinosaurios
#    El primer número es la cantidad de dinosaurios
#    El segundo número es la suma de sus poderes de los dinosaurios que venció
#    El segundo número es la suma de sus poderes de los dinosaurios que venció
#    El segundo número es la suma de sus poderes de los dinosaurios que venció
#   Ejemplo Entrada
#    7123456733102
#   Ejemplo Salida
#    3 67 282 3
#   Ayuda
#    En la primera ronda, el poder Miguelito es $3$
#    En la primera ronda, el poder Miguelito es $3$
#    En la primera ronda, el poder Miguelito es $3$
#    Entonces hay $3$ dinosaurios cuyo poder es $\leq 3$ y la suma de su poder es $1 + 2 + 3 = 6$
#    Entonces hay $3$ dinosaurios cuyo poder es $\leq 3$ y la suma de su poder es $1 + 2 + 3 = 6$
#    Entonces hay $3$ dinosaurios cuyo poder es $\leq 3$ y la suma de su poder es $1 + 2 + 3 = 6$
#    por lo tanto la respuesta es igual a $3$ $6$
#    por lo tanto la respuesta es igual a $3$ $6$
#    por lo tanto la respuesta es igual a $3$ $6$
#    lo mismo para la próxima ronda
#    lo mismo para la próxima ronda
#    lo mismo para la próxima ronda

from bisect import bisect_right

dinos = sorted(int(input()) for _ in range(int(input())))
weights = [0] * len(dinos)
counts = [0] * len(dinos)

for i, dino in enumerate(dinos):
    weights[i] = dino if i == 0 else weights[i-1] + dino
    counts[i] = 1 if i == 0 else counts[i-1] + 1

for _ in range(int(input())):
    Q = int(input())
    index = bisect_right(dinos, Q)
    if index:
        print(counts[index-1], weights[index-1])
    else:
        print(0, 0)