# https://jv.umsa.bo/oj/problem.php?id=2568
#  Moviendo vectores
#  Enviar
#  Estado
#  Descripción
#    Dado un vector de n números donde 2 <= n <= 1000 y un entero k donde 2 <= k <= 200, se pide rotar todos los números que están en las posiciones múltiplos de k incluyendo la primera posicion, hacia la derecha.
#    Dado un vector de n números donde 2 <= n <= 1000 y un entero k donde 2 <= k <= 200, se pide rotar todos los números que están en las posiciones múltiplos de k incluyendo la primera posicion, hacia la derecha.
#    Dado un vector de n números donde 2 <= n <= 1000 y un entero k donde 2 <= k <= 200, se pide rotar todos los números que están en las posiciones múltiplos de k incluyendo la primera posicion, hacia la derecha.
#   Entrada
#    En la primera tendrá los números n y k separados por un espacio
#    La segunda línea tendrá todos los números del vector separados por un espacio.
#   Salida
#    Una única línea de todos los números del vector ya modificado separados por un espacio.
#    Una única línea de todos los números del vector ya modificado separados por un espacio.
#    Una única línea de todos los números del vector ya modificado separados por un espacio.
#   Ejemplo Entrada
#    10 31 2 3 4 5 6 7 8 9 10
#   Ejemplo Salida
#    9 2 1 4 5 3 7 8 6 10
#   Ayuda

n, k = (int(x) for x in input().split(' '))
v = [int(x) for x in input().split(' ')]
aux = v[0]
for i in range(k-1, n, k):
  v[i], aux = aux, v[i]
v[0] = aux
print(*v)