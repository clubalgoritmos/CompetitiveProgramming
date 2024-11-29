# https://jv.umsa.bo/oj/problem.php?cid=2862&pid=0
## https://jv.umsa.bo/oj/problem.php?id=1033
#  Contando Primos
#  Estado
#  Descripción
#    Los números primos son aquellos que son solo divisibles por si mismo o el uno. La lista de los primeros números primos es $2,3,5,7,11,13,17,19....$Dados $0 \leq a, b \leq 10^{7}$ contar cuantos primos hay en ese rango.
#   Entrada
#    La entrada consiste de varios casos de prueba. La primera línea contiene el número de casos de prueba. Las líneas siguientes corresponden a los casos de prueba, cada caso de prueba contiene dos enteros $a$ y $b$, La entrada termina cuando no hay más datos.
#   Salida
#    Para cada caso de prueba su programa debe mostrar, en la salida, una línea con el número de primos existente entre $a$ y $b$ inclusive.
#   Ejemplo Entrada
#    42 1000100000 10000001000000 100000002 10000000
#   Ejemplo Salida
#    16868906586081664579
#   Ayuda
#    Si x es divisible por i : se denota como x%i==0

def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes

def prefix_primes(primes):
    prefix = [0] * len(primes)
    for i in range(1, len(primes)):
        prefix[i] = prefix[i-1] + primes[i]
    return prefix

primes = sieve(10**7)
prefix = prefix_primes(primes)
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(prefix[b] - (prefix[a-1] if a > 0 else 0))
