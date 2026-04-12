# https://jv.umsa.bo/oj/problem.php?id=2804
#  Enviar
#  Estado
#  Descripción
#   Entrada
#   Salida
#   Ejemplo Entrada
#   Ejemplo Salida
#   Ayuda

#NO FUNCIONA
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return {i for i in range(n + 1) if primes[i]}

def sieve_of_fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

primes = sieve_of_eratosthenes(10000)
fibo = sieve_of_fibonacci(1000)
import sys
for i in sys.stdin:
    N = int(i)
    if fibo[N] in primes:
        print('Es primo')
        continue
    print('No es primo')