# https://jv.umsa.bo/oj/problem.php?cid=2815&pid=3
#  Bowling
#  Enviar
#  Estado
#  Descripción
#    Los "bolos" son un juego tradicional en el que los jugadores tratan de derribar el mayor número de bolos posible utilizando, normalmente, una bola.
#    bolos
#    bolos
#    La cantidad de variantes del juego es inmensa, cada una con sus propias normas particulares. La colocación de los bolos, su número, y el objeto que se lanza varía enormemente. En ocasiones, incluso el objetivo cambia; en ciertas modalidades no sólo es importante tirar muchos bolos, sino también conseguir desplazarlos lo más posible desde su posición original.
#    desplazarlos lo más posible
#    La variante más conocida es el bowling, que se juega en lugares cerrados y en el que la bola se desliza por un suelo encerado, en lugar de lanzarla al aire. Al final de la pista, de algo más de 19 metros de largo, se colocan 10 bolos según la disposición siguiente (vista desde arriba):
#    bowling
#    Al golpear un bolo, éste cae y puede derribar a otros. En concreto, para este problema,supondremos que cuando un bolo cae, golpea (y tira) los dos bolos que tiene justo detrás,y éstos hacen lo propio con los siguientes 1. Por ejemplo, si la bola golpea el bolo número 2,éste hará caer a los bolos 4 y 5, y éstos a su vez a los bolos 7, 8 y 9:
#    Al golpear un bolo, éste cae y puede derribar a otros. En concreto, para este problema,
#    supondremos que cuando un bolo cae, golpea (y tira) los dos bolos que tiene justo detrás,
#    y éstos hacen lo propio con los siguientes 1. Por ejemplo, si la bola golpea el bolo número 2,
#    éste hará caer a los bolos 4 y 5, y éstos a su vez a los bolos 7, 8 y 9:
#   Entrada
#    31
#   Salida
#    Para cada caso de prueba se escribirá, en una línea independiente, el número de bolos que quedan de pie tras tirar el bolo indicado, y que éste tire a todos los que tiene detrás. Se garantiza que la salida será siempre menor que 231.
#    Para cada caso de prueba se escribirá, en una línea independiente, el número de bolos que quedan de pie tras tirar el bolo indicado, y que éste tire a todos los que tiene detrás. Se garantiza que la salida será siempre menor que 231.
#    Para cada caso de prueba se escribirá, en una línea independiente, el número de bolos que quedan de pie tras tirar el bolo indicado, y que éste tire a todos los que tiene detrás. Se garantiza que la salida será siempre menor que 2
#    31
#    .
#   Ejemplo Entrada
#    4 2
#   Ejemplo Salida
#    4
#   Ayuda
#    El problema dice que cada fila tiene un pino mas que el anterior, entonce si queremos saber el total de pinos que hay se sabe de esta forma sea f el total de fila, numero total de pinos es (f * (f + 1) )/ 2,
#    El problema dice que cada fila tiene un pino mas que el anterior, entonce si queremos saber el total de pinos que hay se sabe de esta forma sea f el total de fila, numero total de pinos es (f * (f + 1) )/ 2,
#    Conociento esta ecuación puede calcular cuanto son del resultado
#    Conociento esta ecuación puede calcular cuanto son del resultado
#    Ejemplos adicicioneles
#    Ejemplos adicicioneles
#    entradas
#    entradas
#    ---------
#    ---------
#    4 43 1
#    4 43 1
#    Salidas
#    Salidas
#    ----------
#    ----------
#    90
#    90

