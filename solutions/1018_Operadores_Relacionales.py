# Solucion
# https://jv.umsa.bo/oj/problem.php?id=1018
#  Operadores Relacionales
#  Enviar
#  Estado
#  Descripción
#    Algunos operadores verifican la relación entre dos valores y estos operadores se denominan operadores relacionales. Dado dos valores numéricos su trabajo es solamente determinar la relación entre ellos (i) El primero es mayor que el segundo (ii) El primero es menor que el segundo o (iii) El primero y el segundo son iguales.
#   Entrada
#    La primera línea del archivo de entrada es un número entero t (t <15), que indica cuantos pares de números se tiene en la entrada. Cada una de las siguientes t líneas, contiene dos enteros a y b (|a|,|b|<1000000001).
#   Salida
#    Para cada línea de entrada se produce una línea de salida. Esta línea contiene alguno de los siguientes operadores relacionales ">", "<" o "=", el cual indica la relación apropiada entre los dos números.
#   Ejemplo Entrada
#    310 2020 1010 10
#   Ejemplo Salida
#    <>=
#   Ayuda

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")
