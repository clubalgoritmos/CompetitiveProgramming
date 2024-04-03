# https://jv.umsa.bo/oj/problem.php?cid=2819&pid=5
## https://jv.umsa.bo/oj/problem.php?id=2241
#  TRIANGU-LOTE
#  Enviar
#  Estado
#  Descripción
#    Dado un lote, determinar el área de un triángulo por cada 3 números introducidos por teclado, cada 3 números simbolizan los 3 lados del triángulo.
#   Entrada
#    La primera linea contiene un número n $(1 \leq n \leq 3*10^{5})$ (multiplo de 3), el cual indica cuantos números leer.
#    Las siguientes n lineas contiene un único entero x $(1 \leq x \leq 10^{2})$ por linea.
#   Salida
#    Para cada caso de prueba mostrar el área del triángulo.En caso de no haber área imprimir "No hay area"
#   Ejemplo Entrada
#    660724473591
#   Ejemplo Salida
#    Area: 1317.063400No hay area
#   Ayuda
#    Recuerda la formula de heron:
#    https://es.wikipedia.org/wiki/Fórmula_de_Herón

import math
n = int(input())

for i in range(n//3):
    try:
        a = int(input())
        b = int(input())
        c = int(input())
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        if area > 0:
            print("Area: {:.6f}".format(area))
        else:
            raise ValueError
    except ValueError:
        print("No hay area") 