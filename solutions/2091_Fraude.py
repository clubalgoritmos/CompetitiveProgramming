# https://jv.umsa.bo/oj/problem.php?cid=2820&pid=7
## https://jv.umsa.bo/oj/problem.php?id=2091
#  Fraude?
#  Enviar
#  Estado
#  Descripción
#    La ciudad de Springfield actualmente esta en época electoral, después de haber terminado el horario de emisión del voto, Homero como veedor electoral tiene la tarea de verificar que todo este en regla en su recinto.
#    Homero tiene a su disposición $n$ ánforas electorales dispuestas en una fila $a_{0}$ , $a_{1}$, $a_{2}$,..., $a_{n - 1}$, donde $a_{í}$ representa la cantidad de votos emitidos en la $i$-ésima ánfora, Homero considera que hubo irregularidades en la $i$-ésima ánfora si la cantidad de votos de al menos una ánfora mas a la derecha es mayor a esta. Homero quiere saber en cuantas ánforas hubo irregularidades.
#    Por ejemplo si $n = 7$ y $a = [1, 9, 4, 6, 8, 7, 5]$, hubo irregularidades en $3$ ánforas, las cuales son la $a_{0} = 1$ porque mas de una ánfora a su derecha tiene mayor cantidad de votos, $a_{2} = 4$ y $a_{3} = 6$
#    Imprime la cantidad de ánforas con irregularidades.
#   Entrada
#    La primera línea contiene un número entero $t$ ($1 \leq t \leq 10^{2}$)- el número de casos de prueba.
#    Cada caso de prueba consta de dos líneas. La primera línea contiene un número entero n ($1 \leq n \leq 10^{5}$) - el número de ánforas. La segunda línea contiene $n$ números enteros $a_{0}$, $a_{1}$,…, $a_{n - 1}$ ($1 \leq a_{i} \leq 10^{7}$), donde $a_{í}$ representa la cantidad de votos emitidos en la $i$-ésima ánfora.
#    Se garantiza que la suma de todo los casos no excede $2 * 10^{5}$
#   Salida
#    Por cada caso de prueba imprima la cantidad de ánforas electorales en las cuales Homero considera que hubo irregularidades.
#   Ejemplo Entrada
#    571 9 4 6 8 7 522 231 2 3612 10 3 14 9 1144 3 2 1
#   Ejemplo Salida
#    30240
#   Ayuda

for _ in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    c = 0
    max_from_right = A[-1]
    for i in range(N-2, -1, -1):
        if A[i] < max_from_right:
            c += 1
        else:
            max_from_right = A[i]
    print(c)