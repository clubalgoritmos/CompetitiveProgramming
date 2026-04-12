# https://jv.umsa.bo/oj/problem.php?id=1605
#  Serie 5
#  Enviar
#  Estado
#  Descripción
#    Se pide realizar la siguiente serie usando funciones hasta N:
#    $\frac{1!}{1} + \frac{1!}{2} + \frac{2!}{2} + \frac{3!}{3} + \frac{5!}{3} + \frac{8!}{3} + \frac{13!}{4} + \frac{21!}{4} + ... $
#   Entrada
#    Se leera un dato N (1<= N <= 100 ) de entrada que indica cuantos elementos deben ser generados
#   Salida
#    La suma de los elementos hasta N con 2 decimales depresicion (ver ejemplo de salida).
#   Ejemplo Entrada
#    5
#   Ejemplo Salida
#    44.50
#   Ayuda
#    Use doubles
#    TO FIX!!!
#    TO FIX!!!
#    TO FIX!!!

s = 0
fibo = [0, 1]

def fibonacci(n):
    if n<len(fibo):
        return fibo[n]
    else:
        fibo.append(fibonacci(n-1)+fibo[n-2])
        return fibo[n]

def generate_series(n):
    series = []
    for i in range(1, n+1):
        series.extend([i]*i)
    return series

import math

for i in range(int(input())):
    s+=math.factorial(fibonacci(i+1))/generate_series(i+1)[i]
print("{:.2f}".format(s))