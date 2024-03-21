# https://jv.umsa.bo/oj/problem.php?id=1334
#  Ordenando funciones
#  Enviar
#  Estado
#  Descripción
#    Definamos la funcion:
#    Por ejemplo:$$sd(1302) = 6$$Dado un vector de numeros enteros ordena el vector por su valor sd(v[i]) es decir, en vez de comparar por el valor de cada elemento, comparamos por el valor resultante de evaluar cada elemento en la funcion $sd$. Si es que existieran empates(dos numeros con el mismo valor despues de evaluarlos en $sd$), por ejemplo:$$sd(1003) = 4$$y$$sd(121) = 4$$tomamos en cuenta los valores originales, es decir 121 vendria antes que 1003.
#   Entrada
#    En la primera linea de entrada tenemos un numero N que indica el numero de elementos del vector. ($1 <= N <= 100$)En la segunda linea de entrada N numeros enteros que representan los valores del vector. Cada elemento estara entre 1 y 100000
#   Salida
#    Los N numeros originales de le entrada pero ordenados como se describio en la descripción, con un espacio entre cada par de numeros y un salto de linea al final.
#   Ejemplo Entrada
#    51006 7 5 9 11111
#   Ejemplo Salida
#    5 11111 7 1006 9
#   Ayuda

N = int(input())
v = list(map(int, input().split()))
v.sort(key=lambda x: (sum(map(int, str(x))), x))
print(*v)