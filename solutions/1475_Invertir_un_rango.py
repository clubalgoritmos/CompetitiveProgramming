# https://jv.umsa.bo/oj/problem.php?id=1475
#  Invertir un rango
#  Enviar
#  Estado
#  Descripción
#    Se te dará un vector de tamaño N, y dos números i, j se quiere invertir todos los números que estén en el rango i,j. Esto quiere decir:
#    Para el vector [1 2 3 4 5] si pedimos invertir el rango [2,4] quedará [ 1 2 5 4 3].
#   Entrada
#    La primera línea tendrá un número N (1 <= N <= 10000) el tamaño del vector y dos números i,j (0 <= i,j < N) el rango a invertir, la segunda línea contendrá los N elementos del vector.
#   Salida
#    Imprimir los elementos del vector luego de la inversión uno por línea.
#   Ejemplo Entrada
#    5 2 4 1 2 3 4 5
#   Ejemplo Salida
#    12543
#   Ayuda

N, a, b = map(int,input().split())
A = list(map(int,input().split()))
for i in range(abs(a-b)//2+1):
    A[a+i],A[b-i] = A[b-i],A[a+i]
for a in A:
    print(a)