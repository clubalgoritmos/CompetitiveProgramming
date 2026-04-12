#Solucion
import math

def sum_divisores(K):
    suma = 1
    raiz_K = int(math.sqrt(K))
    for i in range(2, raiz_K + 1):
        if K % i == 0:
            suma += i
            if i != K // i:
                suma += K // i
    return suma

N = int(input())
for _ in range(N):
    n = int(input())
    sum_divn = sum_divisores(n)
    sw = False
    print(n, end="")
    if sum_divn == n and n!=1:
        print(" perfecto", end="")
        sw = True
    elif sum_divisores(sum_divn) == n  and n!=1:
        print(" romantico", end="")
        sw = True
    if sum_divn > n:
        print(" abundante", end="")
        sw = True
    if not sw:
        print(" complicado", end="")
    print()