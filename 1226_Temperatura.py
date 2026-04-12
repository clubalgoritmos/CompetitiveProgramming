# https://jv.umsa.bo/oj/problem.php?cid=2815&pid=2
#  Temperatura
#  Enviar
#  Estado
#  Descripción
#   Entrada
#    La entrada consiste en un entero que representa la temperatura en grados Centígrados.
#   Salida
#    Se debe imprimir una o dos lineas, en la primera se debe imprimir: "hace calor", "hace frio", "esta bien" dependiendo del caso, y en la segunda se debe imprimir "hierve" o "se congela" si fuera el caso.
#   Ejemplo Entrada
#    -5
#   Ejemplo Salida
#    hace friose congela
#   Ayuda

N = int(input())
if N>=30:
    print("hace calor")
elif N<10:
    print("hace frio")
else:
    print("esta bien")


if N>=100:
    print("hierve")
elif N<=0:
    print("se congela")