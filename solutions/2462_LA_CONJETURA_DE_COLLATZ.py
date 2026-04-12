# https://jv.umsa.bo/oj/problem.php?cid=2567&pid=7
#  LA CONJETURA DE COLLATZ
#  Estado
#  Descripción
#    La conjetura de Collatz (S) establece lo siguiente: Si tomamos un número natural entero positivo, cualquiera sea la secuencia, esta terminará llegando siempre al número 1.
#    La conjetura de Collatz (S) establece lo siguiente: Si tomamos un número natural entero positivo, cualquiera sea la secuencia, esta terminará llegando siempre al número 1.
#    Sólo se aplican dos operaciones:
#    - Si el número es par, entonces se divide entre 2.
#    (n / 2)
#    - Si el número es impar, se multiplica por 3 y se agrega 1.
#    ( 3*n + 1)
#    Por ejemplo,
#    Si n = 6, la secuencia tiene 8 pasos, obteniendo los siguientes resultados: 3, 10, 5, 16, 8, 4, 2, 1.
#    Si en n = 11, la secuencia tiene 14 pasos: 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
#   Entrada
#    La entrada consiste en múltiples casos de prueba. La primera linea indica cuantos casos de prueba existen. Cada caso de prueba consiste en una sola línea que contiene un entero decimal positivo n <= 106
#    La entrada consiste en múltiples casos de prueba. La primera linea indica cuantos casos de prueba existen. Cada caso de prueba consiste en una sola línea que contiene un entero decimal positivo n <= 10
#    6
#    6
#   Salida
#    Por cada caso de prueba, la salida consta de una sola línea que imprime el número de pasos requeridos para llegar a uno.
#    Por cada caso de prueba, la salida consta de una sola línea que imprime el número de pasos requeridos para llegar a uno.
#   Ejemplo Entrada
#    5261127123456
#   Ejemplo Salida
#    181411161
#   Ayuda

def collatz(n):
    pasos = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        pasos += 1
    return pasos

for _ in range(int(input())): # pylint: disable=unused-variable
    print(collatz(int(input())))
"""
for i in range(int(input())):
    x = int(input())
    y = 0
    while x !=1:
        if not (x % 2) == 0:
            x = (3*x + 1)
        else:
            x = round(x/2)
        y = y+1
    print(y)
"""