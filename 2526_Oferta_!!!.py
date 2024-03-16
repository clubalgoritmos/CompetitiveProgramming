# https://jv.umsa.bo/oj/problem.php?id=2526
#  Oferta !!!
#  Enviar
#  Estado
#  Descripción
#   Entrada
#    La entrada consiste en un numero entero A, 1 ≤ A ≤108 - La eded del usuario.
#   Salida
#    Imprimir"¡Felicidades! Eres elegible para nuestra oferta especial para jovenes" si el usuario tiene entre 18 y 25 años, de lo contrario imprimir "Gracias por tu interes en nuestra oferta especial para jovenes, pero esta oferta es solo para personas entre 18 y 25 años!".
#   Ejemplo Entrada
#    19
#   Ejemplo Salida
#    ¡Felicidades! Eres elegible para nuestra oferta especial para jovenes
#   Ayuda

edad = int(input())
if edad >=18 and edad <25:
    print("¡Felicidades! Eres elegible para nuestra oferta especial para jovenes")
else:
    print("Gracias por tu interes en nuestra oferta especial para jovenes, pero esta oferta es solo para personas entre 18 y 25 aos!")