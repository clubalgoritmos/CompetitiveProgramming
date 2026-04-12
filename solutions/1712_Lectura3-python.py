# https://jv.umsa.bo/oj/problem.php?id=1712
#  Lectura3-python
#  Enviar
#  Estado
#  Descripción
#    El problema consiste en leer todos los datos de cada caso de prueba y imprimir la suma de los mismos en una línea
#   Entrada
#    La entrada consiste de múltiples casos de prueba. Cada caso de prueba comienza con un número entero n que indica cuantos números leer.Luego siguen n lineas cada una con un numero entero. La entrada termina con la palabra fin
#   Salida
#    Imprima en una linea la suma de los n números
#   Ejemplo Entrada
#    123123fin
#   Ejemplo Salida
#    26
#   Ayuda

while True:
    S = input()
    if S=="fin":
        break
    s = 0
    for _ in range(int(S)):
        s+=int(input())
    print(s)