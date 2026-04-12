# https://jv.umsa.bo/oj/problem.php?id=1373
## https://jv.umsa.bo/oj/problem.php?id=1373
#  Clasificación de Caracteres
#  Enviar
#  Estado
#  Descripción
#    Escriba un programa que lea una letra, y diga si esta letra es minúscula, mayúscula. También debe indicar si es una vocal o consonante.Para leer un caracter del teclado se utiliza la siguiente instrucción:char c = (char) System.in.read();
#    En Python ouede leerlo con:c = input()Ejemplo de entrada 1aEjemplo de salida 1minusculavocalEjemplo de entrada 2XEjemplo de salida 2mayusculaconsonante
#   Entrada
#    La entrada consiste de una letra.
#   Salida
#    En la salida escriba si es una letra minúscula o mayúscula. En otra linea escriba si es vocal o consonante.
#   Ejemplo Entrada
#    a
#   Ejemplo Salida
#    minusculavocal
#   Ayuda

S = input()
if S.islower():
    print("minuscula")
else:
    print("mayuscula")
if S.lower() in "aeiou":
    print("vocal")
else:
    print("consonante")