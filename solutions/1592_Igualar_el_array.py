# https://jv.umsa.bo/oj/problem.php?id=1592
#  Igualar el array
#  Enviar
#  Estado
#  Descripción
#    Pepe tiene un array de $n$ enteros definido como $A = a_0, a_1, ..., a_{n-1}$. En una operacion, el puede eliminar un elemento del array. Pepe quiere que todos los elementos del array sean igual a otro. Para esto, el puede eliminar uno o mas elementos del array. Encuentra e imprime el $mínimo$ número de operaciones de eliminación que Pepe debe realizar tal que todos los elementos del array sean iguales.
#   Entrada
#    La primera linea contiene un entero $n(1 \leq n \leq 100)$, denotando el numero de elementos del array $A$.
#    La siguiente línea contiene $n$ números enteros $a_i(0 \leq i < n, 1 \leq a_i \leq 100)$.
#   Salida
#    Imprimir en una linea un entero que denota el mínimo numero de elementos que Pepe debe eliminar para que todos los elementos en el array sean iguales.
#   Ejemplo Entrada
#    53 3 2 1 3
#   Ejemplo Salida
#    2
#   Ayuda

n = input()
A = list(map(int,input().split()))
mx = A[0]
mxn = A.count(mx)
for i in set(A):
    if A.count(i) > mxn:
        mx = i
        mxn = A.count(i)
print(abs(len(A)-mxn))