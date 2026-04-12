# https://jv.umsa.bo/oj/problem.php?id=1375
#  Buscando el Oro
#  Enviar
#  Estado
#  Descripción
#    En este programa debes buscar la primera palabra ORO en una cadena.Luego imprimir la posición donde comienza y donde acaba.
#    En este programa debes buscar la primera palabra ORO en una cadena.Luego imprimir la posición donde comienza y donde acaba.
#    En este programa debes buscar la primera palabra ORO en una cadena.Luego imprimir la posición donde comienza y donde acaba.
#    Por ejemplo en la cadena "abcdefOrOefg" la palabra oro se encuentra desde la posicion 6 hasta la 8.
#    Por ejemplo en la cadena "abcdefOrOefg" la palabra oro se encuentra desde la posicion 6 hasta la 8.
#    Por ejemplo en la cadena "abcdefOrOefg" la palabra oro se encuentra desde la posicion 6 hasta la 8.
#    abcdefOrOefg
#   Entrada
#    La entrada consiste de una cadena enletras mayusculas y minusculas.
#    La entrada consiste de una cadena enletras mayusculas y minusculas.
#    La entrada consiste de una cadena enletras mayusculas y minusculas.
#   Salida
#    Imprima en la salida la posición donde esta la parabra ORO, puede ser en mayusculas o minusculas indistintamente.Sino existe la palabra imprima -1.
#    Imprima en la salida la posición donde esta la parabra ORO, puede ser en mayusculas o minusculas indistintamente.Sino existe la palabra imprima -1.
#    Imprima en la salida la posición donde esta la parabra ORO, puede ser en mayusculas o minusculas indistintamente.Sino existe la palabra imprima
#    ORO
#    -1.
#   Ejemplo Entrada
#    abcdefOrOefg
#   Ejemplo Salida
#    6 8
#   Ayuda

# Buscando oro

x = input().lower()
if "oro" in x:
    i = x.index("oro")
    print(i, i + 2)
else:
    print(-1)