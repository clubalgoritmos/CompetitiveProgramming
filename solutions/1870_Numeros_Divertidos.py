# https://jv.umsa.bo/oj/problem.php?cid=2862&pid=3
## https://jv.umsa.bo/oj/problem.php?id=1870
#  Numeros Divertidos
#  Estado
#  Descripción
#    Los números más divertidos de este año se denominan números triangulares (es decir, enteros que son representables como $\frac{n(n+1)}{2}$, donde k es un número entero positivo), y los números más geniales son aquellos que son representables como una suma de dos números triangulares.
#    Andrew, un conocido hipster, adora todo lo divertido y genial, pero desafortunadamente no es bueno para las matemáticas. Dado el número n, ¡ayúdelo a definir si este número puede ser representado por una suma de dos números triangulares (no necesariamente diferentes)!
#   Entrada
#    La entrada consiste en multiples casos de prueba. La primera linea contiene un entero T, que representa el numero casos de entrada, para cada caso de entrada un numero entero n $(1 \leq n \leq 10^9)$.
#   Salida
#    Para cada caso de entrada imprima SI, si n puede representarse como una suma de dos números triangulares, de lo contrario imprima NO.
#   Ejemplo Entrada
#    2256512
#   Ejemplo Salida
#    SINO
#   Ayuda

def is_triangular(n):
    return ((8*n + 1)**0.5 % 1 == 0)

for _ in range(int(input())):
    n = int(input())
    flag = False
    for i in range(1, int(n**0.5) + 1):
        t = i * (i + 1) // 2
        if is_triangular(n - t):
            flag = True
            break
    print("SI" if flag else "NO")