# https://jv.umsa.bo/oj/problem.php?id=1711
#  Lectura2-python
#  Enviar
#  Estado
#  Descripción
#    El problema consiste en leer todos los datos de cada caso de prueba y imprimir la suma de los mismos en una línea
#   Entrada
#    La entrada consiste de múltiples casos de prueba. La primera linea contiene un numero entero que indica el número de casos de prueba. La primera de cada caso de prueba línea contiene un número entero n que indica cuantos números leer.Luego siguen n lineas cada una con un numero entero.
#   Salida
#    Imprima en una linea la suma de los n números
#   Ejemplo Entrada
#    2123123
#   Ejemplo Salida
#    26
#   Ayuda

for _ in range(int(input())):
    N = int(input())
    s = 0
    for i in range(N):
        s+=int(input())
    print(s)