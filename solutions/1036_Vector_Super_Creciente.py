# https://jv.umsa.bo/oj/problem.php?cid=2822&pid=4
## https://jv.umsa.bo/oj/problem.php?id=1036
#  Vector Super Creciente
#  Enviar
#  Estado
#  Descripción
#    Un vector $A$ de longitud $N$ que contiene numeros enteros positivos se dice que es super creciente si cada elemento es estrictamente mayor que la suma de todos los elementos anteriores.
#    Es decir que para cada $i$ de $2$ a $N$ la condicion es:
#    $A_i > A_1 + A_2 + ... + A_{i-1}$
#    Por ejemplo A = [3, 5, 10, 42] es un vector super creciente, mientras que A = [1, 2, 3] no es ($3 = 1 + 2$ pero deberia ser estrictamente mayor).
#    Reus tenia un vector super creciente $A$ de longitud $N$ con el hace mucho tiempo, pero ahora ha olvidado todos sus elementos.
#    El unico dato que recuerda es que el valor $X$ ocurrio en el indice $k$ del vector, es decir: $A_k = X$.
#    Puedes decirle a Reus si recuerda correctamente?
#    Es decir: existe un vector super creciente $A$ de longitud $N$ tal que $A_k = X$?
#   Entrada
#    La primera linea de cada caso de prueba contiene tres numeros enteros $N$,$k$ y $X$ $(1 \leq k \leq N \leq 2*10^5)$ y $(1 \leq X \leq 10^9)$ donde $N$ es la longitud del vector $A$, $k$ el indice en el que ocurre el valor de $X$.
#   Salida
#    Por cada caso de prueba, genere una nueva linea la respuesta: $SI$ si existe una vector super creciente valido y $NO$ en caso contrario.
#   Ejemplo Entrada
#    43 2 33 3 35 3 66 2 1
#   Ejemplo Salida
#    SINOSINO
#   Ayuda
t = int(input())
for _ in range(t):
    N,k,X = map(int,input().split())
    W = (k*(k+1)/2)
    print("SI" if W<=X else "NO")