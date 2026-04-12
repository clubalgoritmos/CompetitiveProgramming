# https://jv.umsa.bo/oj/problem.php?id=1904
#  Primero y Ultimo
#  Enviar
#  Estado
#  Descripción
#    Dada una cadena imprima los primeros tres caracteres y los tres últimos
#    Dada una cadena imprima los primeros tres caracteres y los tres últimos
#   Entrada
#    La entrada consiste en varios casos de prueba. La primera linea contiene el numero de casos de prueba. Cada caso de prueba consiste en una linea de texto, cuya longitud es mayor igual a seis.
#    La entrada consiste en varios casos de prueba. La primera linea contiene el numero de casos de prueba. Cada caso de prueba consiste en una linea de texto, cuya longitud es mayor igual a seis.
#   Salida
#    Por cada caso de entrada imprima los tres primeros caracteres y los tres últimos.
#    Por cada caso de entrada imprima los tres primeros caracteres y los tres últimos.
#   Ejemplo Entrada
#    3abcdefghi123456789la casa de Juan Jose
#   Ejemplo Salida
#    abc ghi123 789la  ose
#   Ayuda

for _ in range(int(input())):
    A = input()
    print(A[:3],A[-3:])