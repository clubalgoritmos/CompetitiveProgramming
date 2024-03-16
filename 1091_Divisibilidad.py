# https://jv.umsa.bo/oj/problem.php?id=1091
#  Divisibilidad
#  Enviar
#  Estado
#  Descripción
#    Se le darán dos números naturales a y b. Su tarea es verificar si a es divisible por b ó b es divisible por a.
#    Se le darán dos números naturales a y b. Su tarea es verificar si a es divisible por b ó b es divisible por a.
#    Se le darán dos números naturales a y b. Su tarea es verificar si a es divisible por b ó b es divisible por a.
#   Entrada
#    Se le darán muchos casos de prueba.La entrada consta de dos números naturales a y b no mayores a $100$.
#    Se le darán muchos casos de prueba.La entrada consta de dos números naturales a y b no mayores a $100$.
#    Se le darán muchos casos de prueba.La entrada consta de dos números naturales a y b no mayores a $100$.
#   Salida
#    Existen tres posibles respuestas.
#    Existen tres posibles respuestas.
#    Existen tres posibles respuestas.
#    Si a es divisible por b imprimir: "a es divisible por b".
#    Si a es divisible por b imprimir: "a es divisible por b".
#    Si b es divisible por a imprimir: "b es divisible por a".
#    Si b es divisible por a imprimir: "b es divisible por a".
#    Si ninguno de los casos se da imprimir: "-1".
#    Si ninguno de los casos se da imprimir: "-1".
#    Si ninguno de los casos se da imprimir: "-1".
#    Si ninguno de los casos se da imprimir: "-1".
#    Los valores de a y b dependen de la entrada.Imprimir la respuesta en una sola linea.
#    Los valores de a y b dependen de la entrada.Imprimir la respuesta en una sola linea.
#    Los valores de a y b dependen de la entrada.
#    Imprimir la respuesta en una sola linea.
#    Imprimir la respuesta en una sola linea.
#   Ejemplo Entrada
#    5 2552 25 13
#   Ejemplo Salida
#    25 es divisible por 552 es divisible por 2-1
#   Ayuda

import sys
for i in sys.stdin:
    a,b = map(int, i.split())
    if a%b==0:
        print(f"{a} es divisible por {b}")
    elif b%a==0:
        print(f"{b} es divisible por {a}")
    else:
        print(-1)