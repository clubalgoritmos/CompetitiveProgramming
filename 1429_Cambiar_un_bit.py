# https://jv.umsa.bo/oj/problem.php?id=1429
#  Cambiar un bit
#  Enviar
#  Estado
#  Descripción
#    El problema pide cambiar un determinado bit un numero entero. Recordamos que los numeros enteros son de 32 bits.Supongamos que tenemos el numero 10 cuya representación binaria es 1010. Ahora nos piden cambiar el segundo bit a 1, el resultado será 1110 cuya representación decimal es es el 14.
#   Entrada
#    La entrada consiste de un numero entero y el bit que queremos cambiar. En el ejemplo de entrada hay múltiples ejemplos, sin embargo cada caso de prueba solo trae un caso.
#   Salida
#    En la salida escriba en una línea dos números separados por un espacio. El primero el resultado de colocar el bit solicitado a uno y el segundo el resultado de cambiar el bit solicitado, si es uno cambie a 0 y si es cero cambie a 1.
#   Ejemplo Entrada
#    1234 710 310 2
#   Ejemplo Salida
#    1234 110610 214 14
#   Ayuda

while True:
    try:
        n, b = map(int, input().split())
        print(n | 1<<b, n ^ 1<<b)
    except EOFError:
        break
    