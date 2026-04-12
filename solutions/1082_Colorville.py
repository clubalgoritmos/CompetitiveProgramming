# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=5
## https://jv.umsa.bo/oj/problem.php?id=1082
#    Copiado al portapapeles
#  Colorville
#  Enviar
#  Estado
#  Descripción
#    Un simple juego de niños usa un tablero que es una secuencia de cuadrados coloreados. Cada jugador tiene una pieza de juego. Los jugadores alternan turnos, sacando cartas que tienen cada una uno o dos cuadrados coloreados del mismo color. Los jugadores mueven su pieza hacia adelante en el tablero hacia el siguiente cuadrado que haga pareja con el color de la carta, o hacia adelante hasta el segundo cuadrado que haga pareja con el color de la carta que contiene dos cuadrados coloreados, o hacia adelante hasta el último cuadrado en el tablero si no hay un cuadrado con el que emparejar siguiendo la descripción anterior. Un jugador gana si su pieza está en el último cuadrado del tablero. Es posible que no exista ganador después de sacar todas las cartas.
#    En este problema los colores se representan las letras mayúsculas A-Z, a continuación se presenta un ejemplo.
#    Start                             Finish
#    Considere el siguiente deck de cartas: R, B, GG, Y, P, B, P, RR
#    Para 3 jugadores, el juego procede como sigue:
#    Jugador 1 saca R,  se mueve al 1er cuadrado
#    Jugador 2 saca B,  se mueve al 5to cuadrado
#    Jugador 3 saca GG, se mueve al 8vo cuadrado
#    Jugador 1 saca Y,  se mueve al 2do cuadrado
#    Jugador 2 saca P,  se mueve al 11vo cuadrado
#    Jugador 3 saca B,  se mueve al 9no cuadrado
#    Jugador 1 saca P,  se mueve al 4to cuadrado
#    Jugador 2 saca RR, Gano! (no hay R’s al frente de esta pieza así que va hasta el último cuadrado).
#    Usando la misma tabla y el mismo deck de cartas, pero con 2 jugadores, el jugador 1 gana después de 7 cartas. Con 4 jugadores, no hay ganador después de utilizar todas las 8 cartas.
#   Entrada
#    La entrada consiste en información de uno o más juegos. Cada juego comienza con una línea conteniendo el número de jugadores (1-4), el número de cuadrados en el tablero (1-79), y el número de cartas en el deck (1-200). Seguido por una línea de caracteres que representan los cuadrados coloreados del tablero. Seguidos por las cartas en el deck, uno el cada línea. Las Cartas pueden tener una letra o dos de las mismas letras. El final de la entrada esta señalado con una línea que tiene 0 para el número de jugadores – los otros valores son indiferentes.
#   Salida
#    Por cada juego, la salida es el jugador ganador y el número total de cartas usadas, o el número de cartas en el deck, como se muestra en el ejemplo de salida. Siempre use el plural  "cards".
#   Ejemplo Entrada
#    2 13 8RYGPBRYGBRPOPRBGGYPBPRR2 6 5RYGRYBRYYGGB3 9 6QQQQQQQQQQQQQQQQQ0 6 0
#   Ejemplo Salida
#    Player 1 won after 7 cards.Player 2 won after 4 cards.No player won after 6 cards.
#   Ayuda

