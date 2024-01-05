n=int(input())
factoriales = [1]
i = 1
while factoriales[-1] <= n:
    i += 1
    factoriales.append(factoriales[-1] * i)
factoriales.pop()
contador = 0
for f in reversed(factoriales):
    while n >= f:
        n -= f
        contador += 1
print(contador)
