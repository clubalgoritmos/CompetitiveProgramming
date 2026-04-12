# https://jv.umsa.bo/oj/problem.php?id=1710
#  Lectura1-python
#  Enviar
#  Estado
#  Descripción
#    El problema consiste en leer todos los datos y imprimir la suma de los mismos en una línea
#   Entrada
#    La entrada consiste de un caso de prueba, la primera línea contiene un número entero n que indica cuantos números leer.Luego siguen n lineas cada una con un numero entero.
#   Salida
#    Imprima en una linea la suma de los n números
#   Ejemplo Entrada
#    41234
#   Ejemplo Salida
#    10
#   Ayuda

N = int(input())
suma = 0
for _ in range(N):
    suma += int(input())
print(suma)