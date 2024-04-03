# https://jv.umsa.bo/oj/problem.php?cid=2820&pid=8
## https://jv.umsa.bo/oj/problem.php?id=1880
#  Skinny Love
#  Enviar
#  Estado
#  Descripción
#    Hay n individuos numerados del 1 al n, y al individuo con el número i le gusta el individuo con el número $f_i$, donde $(1 \leq fi \leq n)$ y $(fi \neq i)$.
#    Llamamos a un triángulo amoroso una situación en la que al individuo A le gusta el individuo B, al individuo B le gusta el individuo C y al individuo C le gusta el individuo A.
#    El problema requiere averiguar si hay algún triángulo amoroso.
#   Entrada
#    La primera línea contiene un número entero t $(t \leq 100)$: el numero de casos de prueba.
#    Cada caso de entrada contiene un número entero n $(2 \leq n \leq 5000)$: el número de individuos. Seguido n enteros $f_{1}, f_{2}, ..., f_{n} (1 \leq fi \leq n, fi \neq i)$, lo que significa que al i-ésimo individuo le gusta el f-ésimo individuo.
#   Salida
#    Para caso de prueba imprima "YES" si existe un triángulo amoroso. De lo contrario, imprima "NO".
#   Ejemplo Entrada
#    252 4 5 1 355 5 5 5 1
#   Ejemplo Salida
#    YESNO
#   Ayuda

for _ in range(int(input())):
    N = int(input())
    F = list(map(int,input().split()))
    for i in range(N):
        if F[F[F[i]-1]-1]==i+1:
            print("YES")
            break
    else:
        print("NO")