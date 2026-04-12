# https://jv.umsa.bo/oj/problem.php?id=1289
## https://jv.umsa.bo/oj/problem.php?id=1289
#  Lectura1
#  Enviar
#  Estado
#  Descripción
#    Se tiene una lista de números y te piden hallar la suma de los mismos. Se sabe que la suma no excede un numero entero.
#    Se tiene una lista de números y te piden hallar la suma de los mismos. Se sabe que la suma no excede un numero entero.
#    Se tiene una lista de números y te piden hallar la suma de los mismos. Se sabe que la suma no excede un numero entero.
#    Sugerencia
#    Sugerencia
#    Sugerencia
#    Para recorrer todos los casos de prueba se siguiere usar
#    Para recorrer todos los casos de prueba se siguiere usar
#    Para recorrer todos los casos de prueba se siguiere usar
#    for( N=leer.nextInt(),i=0;i<N;i++){
#    for( N=leer.nextInt(),i=0;i<N;i++){
#    for( N=leer.nextInt(),i=0;i<N;i++){
#    //Codigo
#    //Codigo
#    //Codigo
#    }
#    }
#    }
#   Entrada
#    La primera línea contiene un numero $T$ que indica el numero de casos de prueba $0 \leq T \leq 100$.
#    La primera línea contiene un numero $T$ que indica el numero de casos de prueba $0 \leq T \leq 100$.
#    Cada caso de prueba consiste de dos líneas, la primera linea tiene un numero $M$ ($0 \leq M \leq 1000$) que representa la cantidad de números que hay que leer.
#    Cada caso de prueba consiste de dos líneas, la primera linea tiene un numero $M$ ($0 \leq M \leq 1000$) que representa la cantidad de números que hay que leer.
#    La segunda línea contiene los $M$ números separados por un espacio.
#    La segunda línea contiene los $M$ números separados por un espacio.
#   Salida
#    Por cada caso de prueba escrita en una linea la suma de los números.
#    Por cada caso de prueba escrita en una linea la suma de los números.
#    Por cada caso de prueba escrita en una linea la suma de los números.
#   Ejemplo Entrada
#    341 2 3 4109 8 7 6 5 4 3 2 1 -55-1 -3 5 3 1
#   Ejemplo Salida
#    10405
#   Ayuda

for _ in range(int(input())):
    M = int(input())
    print(sum(map(int, input().split())))