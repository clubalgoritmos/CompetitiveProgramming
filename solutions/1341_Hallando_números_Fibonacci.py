# https://jv.umsa.bo/oj/problem.php?id=1341
#  Hallando números Fibonacci
#  Enviar
#  Estado
#  Descripción
#    Los números de Fibonacci se calculan con la fórmula $f_n=f_{n-1}+f_{n-2}$Su tarea es la de imprimir el número Fibonacci correspondiente a un número de entrada. Por ejemplo el tercer Fibonacci es el $2$. Para cada número en la entrada imprima el número Fibonacci correspondiente.
#   Entrada
#    La entrada consiste de números $a<100$ que representa el número de Fibonaci que queremos hallar. Cada número está en una línea. La entrada termina cuando no hay más datos en la entrada.
#   Salida
#    Por cada línea de entrada debe imprimir el número Fibonacci correspondiente en una línea.
#   Ejemplo Entrada
#    47810
#   Ejemplo Salida
#    3132155
#   Ayuda

#hallando fibonacci
import sys
f = []
for i in range(0, 100):
    f.append(0)


def fibo(n):
    if f[n] != 0:
        return f[n]
    if n < 2:
        return n
    else:
        f[n] = fibo(n - 1) + fibo(n - 2)
        return f[n]


if __name__ == '__main__':
    for n in sys.stdin:
        print(fibo(int(n)))