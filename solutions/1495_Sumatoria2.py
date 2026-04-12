# https://jv.umsa.bo/oj/problem.php?cid=2823&pid=6
## https://jv.umsa.bo/oj/problem.php?id=1495
#  Sumatoria2
#  Enviar
#  Estado
#  Descripción
#    Se tiene la siguiente sumatoria:
#    $\frac{1x^{2}}{1}-\frac{3x^{3}}{1}+\frac{6x^{5}}{2}-\frac{10x^{7}}{3}+\frac{19x^{11}}{5}+\dots$
#    Se te pide hallar el resultado de la anterior sumatoria sabiendo cuantos terminos apareceran y el valor de $x$
#   Entrada
#    La entrada conciste de dos numeros enteros $1 \leq n \leq 5$ y $1 \leq x \leq 20$ que representan el numero de elemntos a conciderar en la sumatoria y el valor que toma la variable $x$.
#    La entrada terminara cuando no haya mas elementos por leer.
#   Salida
#    La salida consiste de un número con el resultado de la anterior sumatoria, el número deberáser mostrado con $2$ decimales de precisión.
#   Ejemplo Entrada
#    4 5
#   Ejemplo Salida
#    -251391.67
#   Ayuda
#    Vea la seria de Fibonacci y Tribonacci. y primos.
#    $OK$

n, x = map(int, input().split())
i = 0
s = 0

fibo = [1, 1]
for i in range(2, n):
    fibo.append(fibo[i-1]+fibo[i-2])
tribo = [1,3,6]
for i in range(3, n):
    tribo.append(tribo[i-1]+tribo[i-2]+tribo[i-3])
primos = [1]
for i in range(2, n):
    primos.append(primos[i-1]+i)

while i<n:
    s += tribo[i]*x**(primos[i])/fibo[i]
    i += 1

print("{.:2f}".format(s))
