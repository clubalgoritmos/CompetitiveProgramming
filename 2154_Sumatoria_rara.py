# https://jv.umsa.bo/oj/problem.php?cid=2823&pid=11
## https://jv.umsa.bo/oj/problem.php?id=2154
#  Sumatoria rara
#  Enviar
#  Estado
#  Descripción
#    Dada la siguiente sumatoria:
#    Se te pide hallar el resultado dado un número $n$ y $x$.
#   Entrada
#    La entrada consistirá en $2$ números enteros $n$ ($1 \leq n \leq 8$) la cantidad de elementos a considerar de la sumatoria y $x$ ($1 \leq x \leq 4$) el valor a evaluar dentro de la sumatoria.
#   Salida
#    La salida consiste de un número con el resultado de la sumatoria, debe ser mostrado con $2$ decimales de precisión.
#   Ejemplo Entrada
#    41
#   Ejemplo Salida
#    0.94
#   Ayuda
#    En Java para imprimir con 2 decimales de precisión se debe usarSystem.out.printf("%.2f\n", variableSuma)
#    En Java para imprimir con 2 decimales de precisión se debe usar
#    System.out.printf("%.2f\n", variableSuma)
#    En Python para imprimir con 2 decimales de precisión se debe usarprint("{:.2f}".format(variableSuma))
#    En Python para imprimir con 2 decimales de precisión se debe usar
#    print("{:.2f}".format(variableSuma))

N = int(input())
x = int(input())

def generate_series():
        current_term = 2
        index = 2
        while True:
            yield current_term
            current_term += index
            index += 1

S = 0
for _ in range(N):
    w = generate_series()
    print(next(w)) 
    S += (x) / N
print(S)