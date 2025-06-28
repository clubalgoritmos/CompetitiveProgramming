import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())

bombas = []
elementos = set()

for _ in range(M):
    datos = list(map(int, sys.stdin.readline().split()))
    K, elems = datos[0], datos[1:]
    bombas.append(elems)
    elementos.update(elems)

elementos = sorted(elementos)
mapping = {e: i for i, e in enumerate(elementos)}

bomb_masks = []
for elems in bombas:
    mask = 0
    for e in elems:
        mask |= 1 << mapping[e]
    bomb_masks.append(mask)

dp = defaultdict(int)
dp[0] = 1 

for b in bomb_masks:
    nuevo = defaultdict(int)
    for mask, coef in dp.items():
        nuevo[mask] += coef
        nuevo[mask | b] += coef * (-1)
    dp = nuevo

f = 0
for mask, coef in dp.items():
    popcnt = bin(mask).count("1")
    f += coef / (2 ** popcnt)

resultado = (2 ** N) * f
print(int(resultado))