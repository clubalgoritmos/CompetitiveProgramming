# https://jv.umsa.bo/oj/problem.php?id=1449
#  Vectores1
#  Enviar
#  Estado
#  Descripción
#    Se tiene una lista de números y te piden hallar la suma entre dos valores $a$ y $b$. Se sabe que la suma no excede un numero entero.
#    Se tiene una lista de números y te piden hallar la suma entre dos valores $a$ y $b$. Se sabe que la suma no excede un numero entero.
#    Se tiene una lista de números y te piden hallar la suma entre dos valores $a$ y $b$. Se sabe que la suma no excede un numero entero.
#   Entrada
#    Cada caso de prueba consiste de tres líneas, la primera linea tiene dos números $a$ y $b$ separados por un espacio.
#    Cada caso de prueba consiste de tres líneas, la primera linea tiene dos números $a$ y $b$ separados por un espacio.
#    Cada caso de prueba consiste de tres líneas, la primera linea tiene dos números $a$ y $b$ separados por un espacio.
#    La segunda línea contiene un numero $n$ que representa la cantidad de números que hay que leer.
#    La segunda línea contiene un numero $n$ que representa la cantidad de números que hay que leer.
#    La segunda línea contiene un numero $n$ que representa la cantidad de números que hay que leer.
#    La tercera línea contiene los $n$ números separados por un espacio.
#    La tercera línea contiene los $n$ números separados por un espacio.
#    La tercera línea contiene los $n$ números separados por un espacio.
#   Salida
#    Por cada caso de prueba escrita en una linea la suma de los números cuyo valor están entre $a$ y $b$ inclusive.
#    Por cada caso de prueba escrita en una linea la suma de los números cuyo valor están entre $a$ y $b$ inclusive.
#    Por cada caso de prueba escrita en una linea la suma de los números cuyo valor están entre $a$ y $b$ inclusive.
#   Ejemplo Entrada
#    10 20710 2 10 1 20 31 5
#   Ejemplo Salida
#    40
#   Ayuda

a,b = (int(x) for x in input().split(" "))
n = int(input())
print(sum([int(x) for x in input().split() if (int(x)<=b and int(x)>=a)]))