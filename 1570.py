def fast_modular_exponentiation(b, e, m):
    res = 1
    b %= m

    while e > 0:
        if e & 1:  # Si el bit más a la derecha de e es 1
            res = (res * b) % m
        b = (b * b) % m
        e >>= 1  # Desplaza e un bit a la derecha

    return res

for _ in range(int(input())):
    b,e,m = map(int, input().split())
    print(fast_modular_exponentiation(b, e, m))
