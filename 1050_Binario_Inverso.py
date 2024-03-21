# https://jv.umsa.bo/oj/problem.php?cid=2815&pid=5
#  Binario Inverso
#  Enviar
#  Estado
#  Descripción
#    En colegio están aprendiendo a convertir de decimal a binario. Como es muy aburrido, te has propuesto invertir el equivalente binario y convertir este a decimal. Para esto debes construir un programa.Por ejemplo la representación binaria del numero 13 es 1101 una vez invertido tenemos 1011 que es el numero 11. En el caso del numero 9 su representación es 1001 y el equivalente decimal despues de invertir es 9.
#   Entrada
#    La entrada consiste de varios casos de prueba. Cada caso de prueba es un entero que viene en una sola línea. Termina cuando no hay mas datos en la entrada.
#   Salida
#    Por cada caso de prueba escriba en una línea el equivalente decimal de invertir el numero en binario.
#   Ejemplo Entrada
#    139
#   Ejemplo Salida
#    119
#   Ayuda
while True:
    try:
        I = int(input())
        print(int("0b"+str(bin(I)[2:][::-1]),base=0))
    except:
        break