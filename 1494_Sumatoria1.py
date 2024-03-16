# https://jv.umsa.bo/oj/problem.php?id=1494
#  Sumatoria1
#  Enviar
#  Estado
#  Descripción
#    Se tiene la siguiente sumatoria:
#    Se tiene la siguiente sumatoria:
#    Se tiene la siguiente sumatoria:
#    $\frac{1}{2x}+\frac{1}{3x}+\frac{2}{5x}+\frac{3}{7x}+\frac{5}{11x}+\dots$
#    $\frac{1}{2x}+\frac{1}{3x}+\frac{2}{5x}+\frac{3}{7x}+\frac{5}{11x}+\dots$
#    $\frac{1}{2x}+\frac{1}{3x}+\frac{2}{5x}+\frac{3}{7x}+\frac{5}{11x}+\dots$
#    Se te pide hallar el resultado de la anterior sumatoria sabiendo cuantos terminos aparecerán y el valor de $x$.
#    Se te pide hallar el resultado de la anterior sumatoria sabiendo cuantos terminos aparecerán y el valor de $x$.
#    Se te pide hallar el resultado de la anterior sumatoria sabiendo cuantos terminos aparecerán y el valor de $x$.
#   Entrada
#    La entrada consiste en varios casos de prueba cada prueba consiste de dos numeros enteros $1 \leq n \leq 40$ y $ \leq x \leq 40$ que representan el numero de elementos a considerar en la sumatoria y el valor que toma la variable $x$.
#    La entrada consiste en varios casos de prueba cada prueba consiste de dos numeros enteros $1 \leq n \leq 40$ y $ \leq x \leq 40$ que representan el numero de elementos a considerar en la sumatoria y el valor que toma la variable $x$.
#    La entrada consiste en varios casos de prueba cada prueba consiste de dos numeros enteros $1 \leq n \leq 40$ y $ \leq x \leq 40$ que representan el numero de elementos a considerar en la sumatoria y el valor que toma la variable $x$.
#    La entrada terminara cuando no haya mas elementos por leer.
#    La entrada terminara cuando no haya mas elementos por leer.
#    La entrada terminara cuando no haya mas elementos por leer.
#   Salida
#    La salida consiste de un numero con el resultado de la anterior sumatoria, el numero deberáser mostrado con $2$ decimales de precisión.
#    La salida consiste de un numero con el resultado de la anterior sumatoria, el numero deberáser mostrado con $2$ decimales de precisión.
#    La salida consiste de un numero con el resultado de la anterior sumatoria, el numero deberáser mostrado con $2$ decimales de precisión.
#   Ejemplo Entrada
#    3 1023 6
#   Ejemplo Salida
#    0.12167.88
#   Ayuda
#    Fijese que existen dos secuencias. la de Fibonacci y la de los numeros primos.
#    Fijese que existen dos secuencias. la de Fibonacci y la de los numeros primos.
#    Fijese que existen dos secuencias. la de Fibonacci y la de los numeros primos.
#    $OK$

fibo = [0, 1]
def fibonacci(n):
    if n < len(fibo):
        return fibo[n]
    else:
        fibo.append(fibonacci(n-1) + fibonacci(n-2))
        return fibo[n]

primes = [2]
def nth_prime(n):
    if n <= len(primes):
        return primes[n-1]
    else:
        num = primes[-1] + 1
        while len(primes) < n:
            if all(num % p > 0 for p in primes):
                primes.append(num)
            num += 1
        return primes[-1]

while True:
    try:
        n,x = map(int, input().split())
        s = 0
        for i in range(1,n+1):
            s+=fibonacci(i)/(nth_prime(i)*x)
        print("{:.2f}".format(s))
    except EOFError:
        break