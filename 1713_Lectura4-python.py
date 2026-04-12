# https://jv.umsa.bo/oj/problem.php?id=1713
#  Lectura4-python
#  Enviar
#  Estado
#  Descripción
#    El problema consiste en leer todos los datos de cada caso de prueba y imprimir la suma de los mismos en una línea
#   Entrada
#    La entrada consiste de múltiples casos de prueba, Cada caso de prueba comienza con un número entero n que indica cuantos números leer.Luego siguen n lineas cada una con un numero entero. La entrada termina cuando no hay más datos, que significa fin de archivo.
#   Salida
#    Imprima en una linea la suma de los n números
#   Ejemplo Entrada
#    123123
#   Ejemplo Salida
#    26
#   Ayuda

while True:
    try:
        N = int(input())
        S = 0
        for _ in range(N):
            S+=int(input())
        print(S)
    except EOFError:
        break