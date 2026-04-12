# https://jv.umsa.bo/oj/problem.php?id=1271
#  Curioso muy curioso
#  Enviar
#  Estado
#  Descripción
#   Entrada
#    La entrada consiste de un número entero n, que indica el número de casos, enseguida se tienen n líneas con números enteros positivos que no excedan 1002.
#   Salida
#    Para cada caso se debe reportar Y si es curioso y N si no lo es.
#   Ejemplo Entrada
#    2  145  77
#   Ejemplo Salida
#    YN
#   Ayuda

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