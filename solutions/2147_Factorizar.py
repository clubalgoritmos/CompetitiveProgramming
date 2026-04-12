# https://jv.umsa.bo/oj/problem.php?cid=2862&pid=4
## https://jv.umsa.bo/oj/problem.php?id=2147
#  Factorizar
#  Estado
#  Descripción
#   Entrada
#   Salida
#   Ejemplo Entrada
#    256
#   Ejemplo Salida
#    2(3)*3(1)*5(1)2(4)*3(2)*5(1)
#   Ayuda

def prime_factors(n):
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i] = factors.get(i, 0) + 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

for _ in range(int(input())):
    n = int(input())
    factors = {}
    for i in range(2, n+1):
        for p, count in prime_factors(i).items():
            factors[p] = factors.get(p, 0) + count
    print("".join([f"{k}({v})*" for k, v in sorted(factors.items())])[:-1])
