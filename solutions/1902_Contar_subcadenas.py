# https://jv.umsa.bo/oj/problem.php?id=1902
#  Contar subcadenas
#  Enviar
#  Estado
#  Descripción
#    El problema trata de contar todas las ocurrencias de una cadena en otra. Por ejemplo la cadena xy existe 3 veces en axybxyzxy.
#    El problema trata de contar todas las ocurrencias de una cadena en otra. Por ejemplo la cadena xy existe 3 veces en axybxyzxy.
#   Entrada
#    La entrada consiste en varios casos de prueba. Cada caso de prueba  consiste de dos líneas. La primera línea tiene la cadena. La segunda  contiene la subcadena que queremos contar
#    La entrada consiste en varios casos de prueba. Cada caso de prueba  consiste de dos líneas. La primera línea tiene la cadena. La segunda  contiene la subcadena que queremos contar
#   Salida
#    Por cada caso de entrada imprima en una linea un numero con la cantidad de veces que ocurre la segunda cadena.
#    Por cada caso de entrada imprima en una linea un numero con la cantidad de veces que ocurre la segunda cadena.
#   Ejemplo Entrada
#    2lacasacasacaestoesunproblemae
#   Ejemplo Salida
#    23
#   Ayuda

for _ in range(int(input())):
    S = input()
    s = input()
    print(S.count(s))