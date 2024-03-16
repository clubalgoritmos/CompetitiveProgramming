# https://jv.umsa.bo/oj/problem.php?id=1267
#  Gradas
#  Enviar
#  Estado
#  Descripción
#    Letropolis es un país maravilloso, una de sus grandes bellezas es su arquitectura, por lo mismo dentro de la ciudad principal su mas grande atracción son sus gradas y por el número de visitantes que vienen a verlas no pueden atender a todos. Ellos tienen un juego de adivinanzas para determinar quien visitara estas gradas, el juego consiste en que ellos te dicen un nivel de las gradas y debes decirles cuantas lineas horizontales y verticales existen hasta ese nivel.
#    Letropolis es un país maravilloso, una de sus grandes bellezas es su arquitectura, por lo mismo dentro de la ciudad principal su mas grande atracción son sus gradas y por el número de visitantes que vienen a verlas no pueden atender a todos. Ellos tienen un juego de adivinanzas para determinar quien visitara estas gradas, el juego consiste en que ellos te dicen un nivel de las gradas y debes decirles cuantas lineas horizontales y verticales existen hasta ese nivel.
#    Letropolis es un país maravilloso, una de sus grandes bellezas es su arquitectura, por lo mismo dentro de la ciudad principal su mas grande atracción son sus gradas y por el número de visitantes que vienen a verlas no pueden atender a todos. Ellos tienen un juego de adivinanzas para determinar quien visitara estas gradas, el juego consiste en que ellos te dicen un nivel de las gradas y debes decirles cuantas lineas horizontales y verticales existen hasta ese nivel.
#    Como se aprecia en la fígura de arriba las gradas de se pueden representar en forma de lineas horizontales y verticales, por lo tanto fácilmente se puede contar cuantas de lineas posee cada nivel.Por ejemplo para el nivel $0$ solo existe una línea horizontal de la misma manera el nivel $3$ esta formado por siete lineas cuatro horizontales y tres verticales.
#    Como se aprecia en la fígura de arriba las gradas de se pueden representar en forma de lineas horizontales y verticales, por lo tanto fácilmente se puede contar cuantas de lineas posee cada nivel.Por ejemplo para el nivel $0$ solo existe una línea horizontal de la misma manera el nivel $3$ esta formado por siete lineas cuatro horizontales y tres verticales.
#    Como se aprecia en la fígura de arriba las gradas de se pueden representar en forma de lineas horizontales y verticales, por lo tanto fácilmente se puede contar cuantas de lineas posee cada nivel.Por ejemplo para el nivel $0$ solo existe una línea horizontal de la misma manera el nivel $3$ esta formado por siete lineas cuatro horizontales y tres verticales.
#   Entrada
#    La entrada consiste en varios casos de prueba cada uno conteniendo una número entero $n$ ($0 \leq n \leq 1000$), la entrada termina con $n = -1$(el cual no debe ser procesado).
#    La entrada consiste en varios casos de prueba cada uno conteniendo una número entero $n$ ($0 \leq n \leq 1000$), la entrada termina con $n = -1$(el cual no debe ser procesado).
#    La entrada consiste en varios casos de prueba cada uno conteniendo una número entero $n$ ($0 \leq n \leq 1000$), la entrada termina con $n = -1$(el cual no debe ser procesado).
#   Salida
#    Para cada caso de prueba imprimir un solo número, la cantidad total de lineas en las gradas.
#    Para cada caso de prueba imprimir un solo número, la cantidad total de lineas en las gradas.
#    Para cada caso de prueba imprimir un solo número, la cantidad total de lineas en las gradas.
#   Ejemplo Entrada
#    5120057-1
#   Ejemplo Salida
#    113411115
#   Ayuda
#    while True:  n = int(input())  if n == -1:     break  #codigo para un caso
#    while True:  n = int(input())  if n == -1:     break  #codigo para un caso
#    while True:  n = int(input())  if n == -1:     break  #codigo para un caso

while True:
    n = int(input())
    if n == -1:
        break
    print((n+1)*2-1)