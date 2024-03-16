# Precalcula los factoriales de los dígitos del 0 al 9
factorials = [1]
for i in range(1, 10):
    factorials.append(factorials[-1] * i)

# Función para calcular la suma de los factoriales de los dígitos de un número
def sum_fact(n):
    return sum(factorials[int(i)] for i in str(n))

# Procesa cada número en la entrada
for _ in range(int(input())):
    N = int(input())
    if sum_fact(N) == N:
        print("Y")
    else:
        print("N")