# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=102
## https://jv.umsa.bo/oj/problem.php?id=1552
#    Copiado al portapapeles
#  Concurso de Dulces
#  Enviar
#  Estado
#  Descripción
#    Carlitos es un niño adicto a los dulces. Hasta se subscribió a la revista especializada en dulces que lo escogió para participar en el concurso internacional de escoger dulces.En este concurso existe un número aleatorio de cajas que contienen dulces y esta dispuestas en $M$ filas con $N$ columnas, así que se tienen un total de $M \times N$ cajas. Cada caja tiene un número indicando cuantos dulces contiene.El concursante puede elegir una caja cualquiera y obtener todos los dulces que contiene. Pero siempre hay una trampa, cuando escoge una caja todas las cajas de la filas inmediatamente encima e inmediatamente abajo de la caja escogida, se vacían, así como la caja de la izquierda y la caja de la derecha de la caja escogida.El concursante continúa hasta que no hay más dulces disponibles.La figura siguiente ilustra esto, paso a paso. Cada celda representa una caja y el número de dulces que contiene. En cada paso la caja escogida está en un círculo y las cajas sombreadas son la que se se vacían. Después de ocho pasos el juego se termina y Carlitos escogió $10+9+8+3+7+6+10+1 = 54$ dulces.
#    Para números pequeños de $M$ y $N$, Carlitos puede muy fácilmente hallar el máximo número de dulces que puede escoger, sin embargo cuando los números son altos esta completamente perdido. ¿Puede ayudar a Carlitos a maximizar el número de duluces que puede alzar?
#   Entrada
#    La entrada consiste de varios casos de prueba. La primera línea de cada caso de prueba contiene los enteros positivos $M$ y $N$ ($1 \leq M \times N \leq 10^5$) separados por un espacio, indicando el número de filas y columnas respectivamente. Las siguientes $M$ líneas contienen $N$ enteros separados por un espacio, representando el número inicial de dulces en la caja correspondiente. Inicialmente cada caja tendrá al menos $1$ y como máximo $10^3$ dulces.El final de la entrada se representa por una línea que contiene dos ceros separados por un espacio.
#   Salida
#    Para cada caso de prueba en la entrada, su programa debe imprimir en una sola línea la cantidad máxima de dulces que Carlitos puede alzar.
#   Ejemplo Entrada
#    5 51 8 2 1 91 7 3 5 21 2 10 3 108 4 7 9 17 1 3 1 64 410 1 1 101 1 1 11 1 1 110 1 1 102 49 10 2 75 1 1 50 0
#   Ejemplo Salida
#    544017
#   Ayuda

