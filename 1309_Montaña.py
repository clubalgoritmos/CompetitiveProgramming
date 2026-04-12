# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=54
## https://jv.umsa.bo/oj/problem.php?id=1309
#    Copiado al portapapeles
#  Montaña
#  Enviar
#  Estado
#  Descripción
#    Se define un arreglo A={a[1],a[2],a[3], ..., a[n]} de tipo montaña si cumple las siguientes propiedades.
#    1. Es creciente. Es decir para todo i<n a[i]<a[i+1]2. Es decreciente. Es decir para todo i>n a[i]>a[i+1]3. Es creciente y luego decreciente. Es decir existe un sólo punto i tal que {a[1],a[2],a[3], ..., a[i]} es creciente y {a[i],a[i+1],a[i+2], ..., a[n]} es decreciente.Dado un arreglo A encontrar una subsecuencia S tal que sea una motaña de cardinalidad máxima. Una subsecuencia de un arreglo es un subconjunto de este que conserva el orden.
#   Entrada
#    La primera línea de entrada consiste de un número natural N<=1000 que representa el tamaño del arreglo A. A continueación la siguiente línea contiene números enteros a[1], a[2], a[3], ..., a[n] tal que 0<=a[i]<108.
#   Salida
#    Imprimir la cardinalidad o tamaño del arreglo S.
#   Ejemplo Entrada
#    71 2 1 3 4 2 1
#   Ejemplo Salida
#    6
#   Ayuda

N = int(input())
A = list(map(int, input().split()))

inc = [1] * N
dec = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            inc[i] = max(inc[i], inc[j] + 1)

for i in range(N-2, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j]:
            dec[i] = max(dec[i], dec[j] + 1)

print(max(inc)+ max(dec)-1)