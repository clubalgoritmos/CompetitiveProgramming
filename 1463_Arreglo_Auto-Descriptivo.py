# https://jv.umsa.bo/oj/problem.php?id=1463
#  Arreglo Auto-Descriptivo
#  Enviar
#  Estado
#  Descripción
#    Un arreglo autodescriptivo es un arreglo de n números enteros en [0, n-1], inclusive, tal que cada elemento i'esimo cumple:
#    Un arreglo autodescriptivo es un arreglo de n números enteros en [0, n-1], inclusive, tal que cada elemento i'esimo cumple:
#    A[i]=número de veces que el número i aparece en todo el arreglo A, para todo 0<=i<=n-1.
#    A[i]=número de veces que el número i aparece en todo el arreglo A, para todo 0<=i<=n-1.
#    Por ejemplo un posible arreglo autodescriptivo de tamaño 5 es:
#    Por ejemplo un posible arreglo autodescriptivo de tamaño 5 es:
#    A = 2, 1, 2, 0, 0
#    A = 2, 1, 2, 0, 0
#    pos:0 1 2 3 4
#    pos:0 1 2 3 4
#    A[0]=2, significa que existen dos valores iguales a 0 en el arreglo.
#    A[0]=2, significa que existen dos valores iguales a 0 en el arreglo.
#    A[1]=1, significa que existe un valor igual a 1 en el arreglo.
#    A[1]=1, significa que e
#    xiste un valor igual a 1 en el arreglo.
#    A[2]=2, significa que existen dos valores iguales a 2 en el arreglo.
#    A[2]=2, significa que e
#    xisten dos valores iguales a 2 en el arreglo.
#    A[3]=0, significa que no existe ningún valorn igual a 3.
#    A[3]=0, significa que n
#    o existe ningún valorn igual a 3.
#    A[4]=0, significa que no existe ningún valor igual a 4.
#    A[4]=0, significa que n
#    o existe ningún valor igual a 4.
#   Entrada
#    Un número entero positivo n<=1000.
#    Un número entero positivo n<=1000.
#   Salida
#    Imprimir un arreglo autodescriptivo de tamaño n, en el caso de existir varias respuestas escoger la mayor lexicográficamente (Es decir que su valor en base n sea el máximo posible). Cada elemento debe ir en una distinta línea y en orden. Si no existe tal arreglo imprimir -1.
#    Imprimir un arreglo autodescriptivo de tamaño n, en el caso de existir varias respuestas escoger la mayor lexicográficamente (Es decir que su valor en base n sea el máximo posible). Cada elemento debe ir en una distinta línea y en orden. Si no existe tal arreglo imprimir -1.
#   Ejemplo Entrada
#    10
#   Ejemplo Salida
#    6210001000
#   Ayuda
#    Ejemplo de Entrada1Ejemplo de salida-1--------------------------------------------------------------
#    En el primer ejemplo de salida se ve el arreglo autodescriptivo de tamaño 10 (ya que es único es el mayor lexicográficamente).
#    A = 6 2 1 0 0 0 1 0 0 0
#    pos:0 1 2 3 4 5 6 7 8 9
#    A[0] = 6significa que existen seis valores iguales a 0 en el arreglo.
#    A[1] = 2 significa que existen dos valores iguales a 1 en el arreglo.
#    A[6] = 1 significa que existe un valor igual a 6 en el arreglo.
#    Todos los demás A[i] son iguales a cero ya que nunca aparecen en el arreglo..
#    En el segundo ejemplo de salida se ve que no existe ningún posible arreglo auto descriptivo de tamaño 1, lo únicos candidatos son {0} el cual no es posible ya que A[0]=0 se contradice ya que la cantidad de 0's es en realidad 1 y en el arreglo {1} la posición 1 no existe. Por lo tanto se imprime -1.

#no funcioan

N = int(input())
A = [0]*N
A[0]=N
def correcto():
    for i in range(N):
        if A[i] != A.count(i):
            return False
    return True

if N == 1:
    print("-1")
else:
    while not correcto():
        last = A.copy()
        for i in range(N):
            A[i] = A.count(i)
        if last == A:
            print("-1")
            break
    else:
        for a in A:
            print(a, end="\n")