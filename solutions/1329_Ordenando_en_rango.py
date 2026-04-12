#  https://jv.umsa.bo/oj/problem.php?id=1329
#  Ordenando en rango
#  Enviar
#  Estado
#  Descripción
#    Dado un vector $A$ de enteros se le pide ordenar todos los elementos del vector que se encuentran entre los indices $I$ y $J$ (incluidos los que se encuentran en $I$ y $J$). Los indices del vector se manejan desde 0.
#   Entrada
#    En la primera linea de la entrada se encuentran $3$ enteros $N$, $I$, $J$ ($1 <= N <= 100$, $0 <= I <= J <= N-1$) separados por un espacio.En la segunda linea de la entrada $N$ numeros enteros $A_i$ separados por un espacio que son los elementos del vector $A$. ($0$ $<=$ $A_i$ $<=$ $1000000$)
#   Salida
#    Los $N$ elementos del vector $A$ separados por un espacio despues de ordenar los elementos que se encuentran entre los indices $I$ y $J$. Y un salto de linea al final de todos los numeros.
#   Ejemplo Entrada
#    10 4 83 1 2 4 5 6 2 7 1 0
#   Ejemplo Salida
#    3 1 2 4 1 2 5 6 7 0
#   Ayuda

N,I,J = map(int,input().split())
A = list(map(int,input().split()))
x = A[:I] + sorted(A[I:J+1]) + A[J+1:]
print(*x)