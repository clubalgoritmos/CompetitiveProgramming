# https://jv.umsa.bo/oj/problem.php?id=1383
#  Cola de Impresión
#  Enviar
#  Estado
#  Descripción
#    La única impresora en la oficina tiene un carga de trabajo muy elevada. Algunas veces hay cientos de trabajo en la cola de impresión, y puede que tenga que esperar horas para tener sus listados. Dado que algunos trabajos son más importantes que otros, se ha implementado un sistema simple de prioridades para la cola de impresión. Ahora cada trabajo es asignado con un número entre $1$ y $9$ siendo el numero $9$ el de mayor prioridad. Esta cola opera como sigue:
#    El primer trabajo se saca de la cola
#    Si existe un trabajo en la cola con prioridad mayor que el trabajo $j$ mueva el trabajo $j$ al final de la cola.
#    En otro caso imprima $j$ y sáquelo de la cola
#    Con este método los trabajos del jefe se imprimirán muy rápido y el resto es posible que tenga que esperar mucho tiempo. Así es la vida.Tu problema con esta nueva política es que se ha vuelto difícil de determinar cuando saldrá su impresión. Así que tienes que hacer un programa que dada la cola determines y tu posición en la cola determines cuanto tiempo debes esperar para obtener tu listado. Para este problema consideraremos que cada impresión dura un minuto..Considere que la cola no cambia y que agregar y quitar trabajos es instantáneo.
#   Entrada
#    La entrada comienza con un número positivo $t$ indicando el numero de casos de prueba a lo máximo $100$.Cada caso de prueba consiste de una linea con dos enteros $n,m$ donde $n$ es el numero de trabajos en la cola y $m$ la posición de su trabajo, seguidos de una linea que contiene los $n$ elementos de la cola.
#   Salida
#    Por cada caso de prueba escriba en una linea el numero entero que representa el número de minutos que debe esperar.
#   Ejemplo Entrada
#    31 054 21 2 3 46 01 1 9 1 1 1
#   Ejemplo Salida
#    125
#   Ayuda

for _ in range(int(input())):
    n, m = map(int,input().split())
    q = list(map(int,input().split()))
    for q_i in range(n):
        q[q_i] = (q[q_i], q_i)
    time = 0
    x = q[m]
    while True:
        if q[0][0] == max(q, key=lambda x: x[0])[0]:
            time += 1
            if q[0][1] == m:
                break
            q.pop(0)
        else:
            q.append(q.pop(0))
    print(time)