# https://jv.umsa.bo/oj/problem.php?id=1907
## https://jv.umsa.bo/oj/problem.php?id=1907
#  Remplazar todas las ocurrencia
#  Enviar
#  Estado
#  Descripción
#    El problema trata de remplazar todas las ocurrencias de caracteres de una cadena por otra.Por ejemplo cambiar los caracteres ca de lacasacasa por xyz para tener laxyzsaxyzsa.
#   Entrada
#    La entrada consiste en varios casos de prueba. Cada caso de prueba consiste de dos lineas. La primera línea tiene la cadena en la que queremos cambiar caracteres y la segunda línea contiene dos cadenas separadas por un espacio. La primera cadena contiene los caracteres a buscar y la segunda los caracteres que remplazar.
#   Salida
#    Por cada caso de entrada imprima la cadena original modificada
#   Ejemplo Entrada
#    2lacasacasaca xyzestoesunproblemae x
#   Ejemplo Salida
#    laxyzsaxyzsaxstoxsunproblxma
#   Ayuda

for _ in range(int(input())):
    S = input()
    a,b = input().split()
    #print(S.translate(str.maketrans(a,b)))
    print(*S.split(a), sep=b)