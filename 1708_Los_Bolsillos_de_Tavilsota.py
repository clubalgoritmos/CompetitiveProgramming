# https://jv.umsa.bo/oj/problem.php?id=1708
#  Los Bolsillos de Tavilsota
#  Enviar
#  Estado
#  Descripción
#    Tavilsota tiene n monedas, el valor de la moneda i-th es ai. Tavilsota quiere distribuir todas las monedas entre sus bolsillos, pero no puede poner dos monedas con el mismo valor en el mismo bolsillo.
#    Por ejemplo, si Tavilsota tiene seis monedas representadas como un arreglo = $[1,2,4,3,3,2]$, puede distribuir las monedas en dos bolsillos de la siguiente manera: $[1,2,3]$, $[2 , 3,4]$.
#    Tavilsota quiere distribuir todas las monedas con el número mínimo de bolsillos usados. Ayúdale a hacer eso.
#   Entrada
#    El problema tiene varios casos de pruebaLa primera línea de la entrada contiene un entero $n$ ($1 \leq n \leq 100$) - el número de monedas.
#    La segunda línea de la entrada contiene $n$ enteros $a_{1}$, $a_{2}$,…, $a_{n}$ ($1 \leq a_{i} \leq 100$) - valores de monedas.
#   Salida
#    Imprima solo un número entero: el número mínimo de bolsillos que Tavilsota necesita para distribuir todas las monedas, de modo que no se pongan dos monedas con el mismo valor en el mismo bolsillo.
#   Ejemplo Entrada
#    61 2 4 3 3 21100
#   Ejemplo Salida
#    21
#   Ayuda

import sys
if __name__ == "__main__":
    for line in sys.stdin:      #lectura hasta el fin de archivo
        mayor = 0
        l = input()
        l = l.split()
        for i in l:
            a = l.count(i)      #obtenemos la cantidad de repeticiones que tiene cada numero
            if(a>mayor):        #el mayor es el que buscamos
                mayor = a
        if(mayor > 0):
            print(mayor)