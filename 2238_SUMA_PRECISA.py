# https://jv.umsa.bo/oj/problem.php?cid=2823&pid=4
## https://jv.umsa.bo/oj/problem.php?id=2238
#  SUMA PRECISA
#  Enviar
#  Estado
#  Descripción
#    Evaluar la siguiente sumatoria:
#    $\frac{4}{2} + \frac{7}{4} + \frac{11}{6} + \frac{16}{8} + \frac{23}{10} + \frac{33}{12} + \frac{48}{14} + \frac{71}{16} + ...$
#   Entrada
#    La entrada tiene varios casos de prueba.Cada caso de prueba contiene un solo entero $N$ $(1 \leq N \leq 44)$ la cantidad de terminos de la sumatoria a evaluar
#   Salida
#    Por cada caso de prueba imprime $S$ con 4 decimales.
#   Ejemplo Entrada
#    51
#   Ejemplo Salida
#    9.88332.0000
#   Ayuda
#    4 / 2 = 2.07 / 4 = 1.7511 / 6 = 1.833333333333333316 / 8 = 2.023 / 10 = 2.3

def calcular_diferencia(n):
    if n == 1:
        return 3
    else:
        return calcular_diferencia(n - 1) + n

def calcular_iesimo_numero(i):
    if i == 1:
        return 4
    else:
        return calcular_iesimo_numero(i - 1) + calcular_diferencia(i - 1)


while True:
    try:
        N = int(input())
        S = 0
        for i in range(1,N+1):
            S+=calcular_iesimo_numero(i)/(2*i)
        print("{:.4f}".format(S))
    except EOFError:
        break