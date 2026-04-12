# https://jv.umsa.bo/oj/problem.php?cid=2825&pid=1
## https://jv.umsa.bo/oj/problem.php?id=1916
#  Lotes 2
#  Enviar
#  Estado
#  Descripción
#    Dado un lote de $n$ numeros, determinar cuantos números primos hay en el lote.
#   Entrada
#    La primera linea contiene un número $n$ ($1 \leq n \leq 1000$), el cual indica cuantos números leer.
#    Las siguientes $n$ lineas contienen un $n$-ésimo número por linea. ($1 \leq n_{i} \leq 1000$)
#   Salida
#    Imprima cuantos números primos existen en el lote.
#   Ejemplo Entrada
#    5422719176
#   Ejemplo Salida
#    2
#   Ayuda
p = 0
for _ in range(int(input())):
    N = int(input())
    for i in range(2,N):
        if N%i==0:
            break
    else:
        p += 1
print(p)