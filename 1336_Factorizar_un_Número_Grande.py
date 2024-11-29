# https://jv.umsa.bo/oj/problem.php?cid=2862&pid=2
## https://jv.umsa.bo/oj/problem.php?id=1336
#  Factorizar un Número Grande
#  Estado
#  Descripción
#    Se tiene un número compuesto $2 \leq n \leq 2^{31}$. Hallar sus factores primos.Como ejemplo los factores primos de $36$ son $2,2,3,3$.Si el número es primo por ejemplo el número $7$ se imprimirá un solo factor el $7$.
#   Entrada
#    La entrada consiste de varios casos de prueba. En cada línea se tiene un número entero positivo compuesto.La entrada termina cuando no hay más datos.
#   Salida
#    Para cada caso de prueba escriba los factores primos del número en una sola línea separados por un espacio.
#   Ejemplo Entrada
#    361504703107600851475143
#   Ejemplo Salida
#    2 2 3 3 150470310771 839 1471 6857
#   Ayuda

while True:
    try:
        n = int(input())
        i = 2
        factors = []
        while i * i <= n:
            while n % i == 0:
                n //= i
                factors.append(str(i))
            i += 1
        if n > 1:
            factors.append(str(n))
        print(" ".join(factors))
    except EOFError:
        break