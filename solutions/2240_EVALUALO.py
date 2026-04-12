# https://jv.umsa.bo/oj/problem.php?cid=2826&pid=17
## https://jv.umsa.bo/oj/problem.php?id=2240
#  EVALUALO
#  Enviar
#  Estado
#  Descripción
#    Evaluar la siguiente sumatoria:$2 - 1 + 4 - 3 + 6 - 5 = 3$
#    El ejemplo es para N =6.
#    Ahora bien, para el valor de N=12 la secuencia y total sería:
#    $2 - 1 + 4 - 3 + 6 - 5 + 8 - 7 + 10 - 9 + 12 - 11 = 6$
#   Entrada
#    La entrada contiene un único entero $N$ $(1 \leq N \leq 10^{4})$
#   Salida
#    La salida contiene los términos que se usaron en la sumatoria, acompañado del símbolo '=' y a continuación el acumulado de la suma.
#   Ejemplo Entrada
#    6
#   Ejemplo Salida
#    2 - 1 + 4 - 3 + 6 - 5 = 3
#   Ayuda

N = int(input())
S = []
for i in range(N):
    if i%2==0:
        S.append(i+2)
        continue
    S.append(-i)
print(*S, sep="+", end="=")