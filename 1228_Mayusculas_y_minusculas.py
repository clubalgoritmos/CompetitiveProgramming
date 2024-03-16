# https://jv.umsa.bo/oj/problem.php?id=1228
#  Mayusculas y minusculas
#  Enviar
#  Estado
#  Descripción
#    Se pide que lea una letra y si es minúscula la convierta en mayúscula y viceversa.
#    Para leer un caracter del teclado se utiliza la siguiente instrucción:char c = (char) System.in.read();
#   Entrada
#    La entrada consiste de una letra en una linea.
#   Salida
#    La salida consiste de una letra de acuerdo al enunciado.
#   Ejemplo Entrada
#    a
#   Ejemplo Salida
#    A
#   Ayuda

fun = lambda x: (x.upper() if x.islower() else x.lower())
print(''.join(map(fun, input())))