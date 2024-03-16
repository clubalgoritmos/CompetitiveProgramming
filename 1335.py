import sys

# Precomputar los factoriales
factorial = [1]
for i in range(1, 6):
    factorial.append(factorial[-1] * i)

for line in sys.stdin:
    N = line.strip()
    if N == '0':
        break
    N = N[::-1]  # Invertir la cadena para facilitar el cálculo
    decimal = sum(int(N[i]) * factorial[i + 1] for i in range(len(N)))
    print(decimal)