# https://jv.umsa.bo/oj/problem.php?cid=2567&pid=8
#  SUBSECUENCIA PALÍNDROMA
#  Estado
#  Descripción
#    A partir de un vector v que consta de n números enteros,determinar si este vector tiene subsecuencias de al menos 3 elementos, que sea un palíndromo.
#    Recuerda que un vector b se denomina subsecuencia del vector a,si b se puede obtener de a, eliminando algunos elementos (posiblemente cero) de a (no necesariamente consecutivos), sin cambiar el orden de los elementos restantes.
#    Por ejemplo, si el vector a fuera [1,2,1,3]
#    son subsecuencias de a los siguientes vectores: [2], [1,2,1], [1,2,1,3], [2,3]
#    mientras que las siguientes NO lo son: [4],[1,1,2],[1,3,1]
#    Ahora bien, un palíndromo es aquella frase o palabra que se lee igual hacia atrás que hacia adelante. Y un vector palíndromo, tendrá la misma lógica, es decir, que se lee igual hacia atrás que hacia adelante.
#    En el ejemplo, la segunda subsecuencia [1,2,1], califica como un vector palíndromo, puesto que se lee igual hacia adelante y hacia atrás.
#   Entrada
#    La primera línea de la entrada contiene un número enterok, que representael número de casos de prueba.
#  La primera línea de la entrada contiene un número enterok, que representael número de casos de prueba.
#    La primera línea de la entrada contiene un número enterok, que representa
#    La primera línea de la entrada contiene un número entero
#    k
#    k
#    , que representa
#    el número de casos de prueba.
#    el número de casos de prueba.
#    Las siguientes líneasdescriben los casos de prueba.
#  Las siguientes líneasdescriben los casos de prueba.
#    Las siguientes líneasdescriben los casos de prueba.
#    Las siguientes líneasdescriben los casos de prueba.
#    La primera línea del caso de prueba contiene un número entero nque es la longitud del vector a.
#    La primera línea del caso de prueba contiene un número entero n
#    La primera línea del caso de prueba contiene un número entero
#    n
#    n
#    que es la longitud del vector a.
#    a
#    La segunda línea del caso de prueba contiene nnúmeros enteros, del vector a.
#    La segunda línea del caso de prueba contiene nnúmeros enteros, del vector a.
#    La segunda línea del caso de prueba contiene
#    n
#    núme
#    ros enteros, del vector a.
#    a
#   Salida
#    Para cada caso de prueba, imprima la respuesta: "TIENE"(sin comillas) si el vector a tiene alguna subsecuencia de al menos 3 elementos que es un palíndromo y "NO TIENE"(sin comillas) en caso contrario.
#    Para cada caso de prueba, imprima la respuesta: "TIENE"(sin comillas) si el vector a tiene alguna subsecuencia de al menos 3 elementos que es un palíndromo y "NO TIENE"(sin comillas) en caso contrario.
#    Para cada caso de prueba, imprima la respuesta: "
#    "(sin comillas) si el vector a tiene alguna subsecuencia de al menos 3 elementos que es un palíndromo y "
#    "(sin comillas) en caso contrario.
#   Ejemplo Entrada
#    431 2 151 2 2 3 241 2 2 1101 1 2 2 3 3 4 4 5 5
#   Ejemplo Salida
#    TIENETIENETIENENO TIENE
#   Ayuda

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    sw=False
    for i in range(n):
        for j in range(i+1, n+1):
            x = arr[i:j]
            if x == x[::-1] and len(x) > 2:
                print('TIENE')
                sw=True 
                break
        if sw:
            break
    if not sw:
        print('NO TIENE')
    