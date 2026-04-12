# https://jv.umsa.bo/oj/problem.php?id=1433
#  Primos en un rango
#  Enviar
#  Estado
#  Descripción
#    Se debe contar cuántos primos existen entre dos números A y B, por ejemplo entre 1 y 10 existen 4 primos: 2,3,5,7
#   Entrada
#    Se te dará dos números A,B (1<=A <= B<= 1000).
#   Salida
#    Imprimir el número de primos en el rango [A,B]
#   Ejemplo Entrada
#    1 10
#   Ejemplo Salida
#    4
#   Ayuda

a, b = map(int, input().split())
c = 0
for i in range(a, b + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            c += 1
print(c)