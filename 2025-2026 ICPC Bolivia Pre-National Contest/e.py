import sys
import bisect

data = sys.stdin.read().split()
N = int(data[0])
T = int(data[1])
tiempos = list(map(int, data[2:]))

mitad = N // 2
grupo1 = tiempos[:mitad]
grupo2 = tiempos[mitad:]

suma_grupo1 = []
suma_grupo2 = []

n1 = len(grupo1)
for mask in range(1 << n1):
    s = 0
    for i in range(n1):
        if mask & (1 << i):
            s += grupo1[i]
    if s <= T:
        suma_grupo1.append(s)

n2 = len(grupo2)
for mask in range(1 << n2):
    s = 0
    for i in range(n2):
        if mask & (1 << i):
            s += grupo2[i]
    if s <= T:
        suma_grupo2.append(s)

suma_grupo2.sort()
mejor = 0
for s1 in suma_grupo1:
    restante = T - s1
    idx = bisect.bisect_right(suma_grupo2, restante)
    if idx:
        candidato = s1 + suma_grupo2[idx - 1]
        if candidato > mejor:
            mejor = candidato
print(mejor)
