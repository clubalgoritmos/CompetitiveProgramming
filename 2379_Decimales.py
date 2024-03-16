# https://jv.umsa.bo/oj/problem.php?id=2379
#  Decimales
#  Enviar
#  Estado
#  Descripción
#    Dado un número n, primero debe verificar si es primo. Si no es un número primo imprima el número seguido de dos puntos y luego de un espacio imprimir -1.En el caso de que el número sea primo, imprima el número seguido de dos puntos y después de un espacio los primeros 40 decimales de 1/n.
#    Dado un número n, primero debe verificar si es primo. Si no es un número primo imprima el número seguido de dos puntos y luego de un espacio imprimir -1.En el caso de que el número sea primo, imprima el número seguido de dos puntos y después de un espacio los primeros 40 decimales de 1/n.
#   Entrada
#    La entrada consiste de múltiples casos de prueba. La primera linea contiene el numero de casos de prueba. Luego siguen los casos de prueba que son números entre 3 y 999.
#    La entrada consiste de múltiples casos de prueba. La primera linea contiene el numero de casos de prueba. Luego siguen los casos de prueba que son números entre 3 y 999.
#   Salida
#    Imprima en la salida lo especificado de acuerdo al formato del ejemplo.
#    Imprima en la salida lo especificado de acuerdo al formato del ejemplo.
#    Al final de la linea existe un espacio en blanco
#    Al final de la linea existe un espacio en blanco
#   Ejemplo Entrada
#    2819
#   Ejemplo Salida
#    8: -119: 0 5 2 6 3 1 5 7 8 9 4 7 3 6 8 4 2 1 0 5 2 6 3 1 5 7 8 9 4 7 3 6 8 4 2 1 0 5 2 6
#   Ayuda

from decimal import Decimal, getcontext
for i in range(int(input())):
    num = int(input())
    for n in range(2, num):
        if num % n == 0 and n!=-1:
            print(f"{num}: -1")
            break
        elif n == num-1:
            getcontext().prec = 45
            var = list(str(f"{Decimal(1)/Decimal(num):.41f}"))
            var.pop(41)
            var.pop(0)
            var.pop(0)
            print(f'{num}:', ' '.join(var), '')