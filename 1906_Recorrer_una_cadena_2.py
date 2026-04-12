# https://jv.umsa.bo/oj/problem.php?id=1906
#  Recorrer una cadena 2
#  Enviar
#  Estado
#  Descripción
#    El problema trata de recorrer una cadena y imprimir sus caracteres de acuerdo al formato mostrado.
#   Entrada
#    La entrada consiste en varios casos de prueba. La primera linea contiene el numero de casos de prueba. Cada caso de prueba consiste en una linea de texto.
#   Salida
#    Por cada caso de entrada imprima la entrada como se muestra en el ejemplo.
#   Ejemplo Entrada
#    1abcdefghi
#   Ejemplo Salida
#    a,b,c,d,e,f,g,h,i
#   Ayuda

for _ in range(int(input())):
    S = input()
    print(*S,sep=',')