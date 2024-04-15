# https://jv.umsa.bo/oj/problem.php?id=1487
#  modular3
#  Enviar
#  Estado
#  Descripción
#    A Talvisota se le pidio realizar una función que verifique si un número leído por teclado es primo o no
#   Entrada
#    La entrada consiste en varios numeros leidos por teclado
#   Salida
#    por cada linea de entrada se debe mostrar "ES PRIMO" o "NO ES PRIMO" si no es el caso
#   Ejemplo Entrada
#    417123
#   Ejemplo Salida
#    NO ES PRIMOES PRIMONO ES PRIMO
#   Ayuda
#    Se puede tener una funcion o procedimiento para verificar si el numero es primo o no
#    primos son los numeros que cuyos unicos divisores son el 1 y el mismo numero

import math

while True:
    try:
        n = int(input())
        if n < 2:
            print("NO ES PRIMO")
        else:
            for i in range(2, math.isqrt(n) + 1):
                if n % i == 0:
                    print("NO ES PRIMO")
                    break
            else:
                print("ES PRIMO")
    except EOFError:
        break