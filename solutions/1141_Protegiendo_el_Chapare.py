# https://jv.umsa.bo/oj/problem.php?cid=2826&pid=6
## https://jv.umsa.bo/oj/problem.php?id=1141
#  Protegiendo el Chapare
#  Enviar
#  Estado
#  Descripción
#    Se ha instalado una red de estaciones de vigilancia que funcionan con baterías, para proteger las áreas protegidas del Chapara. La batería es un elemento critico, y debe durar la mayor cantidad de tiempo. Con el propósito de ahorrar energía, bajando la potencia de transmisión, una estación solo puede transmitir a dos estaciones. Los destinatarios son las estaciones que estén en lo más próximas. En caso de que dos estaciones se encuentren a la misma distancia primero se transmite a la que esta más al oeste, y luego a la más del sur.
#    Usted ha sido asignado la tarea de escribir un programa que decida, dada la localización de cada estación, enviando un mensaje desde la primera estación si los mensajes llegan a todas las estaciones.
#    Cuando un mensaje llega a todas las estaciones decimos que el Chapare esta protegido.
#   Entrada
#    La entrada consiste de un entero N seguido por N pares de enteros Xi,Y i indicando la localización de las coordenadas de cada estación. El primer par de coordenadas determina la primera estación que hará el mensaje. Los siguientes N − 1 pares son las coordenadas de posición de de cada una de las otras estaciones. Las restricciones son ( − 20 ≤ Xi,Y i ≤ 20) y (1 ≤ N,≤ 1000). Los datos de entrada terminan cuando N = 0.
#   Salida
#    Por cada caso de entrada deberá imprimir la frase ”Chapare protegido” cuando todas las estaciones son alcanzables y ”Chapare no Protegido”, en otros casos.
#   Ejemplo Entrada
#    41 00 1-1 00 -181 01 10 1-1 1-1 0-1 -10 -11 -160 30 41 3-1 3-1 -4-2 -50
#   Ejemplo Salida
#    Chapare protegidoChapare protegidoChapare no Protegido
#   Ayuda
#    En el primer ejemplo tenemos 4 estaciones ubicadas en los puntos de los ejes cartesianos. Hallamos las distancias entre cada punto con la formula de la distancia entre dos punto X(i,j) y Y(i,j). Con estas distancias armamos el grafo de las conexiones que será un grafo dirigido, con el que se resolverá el problema.
while True:
    N = int(input())
    if N==0:
        break
    for i in range(N):
        x,y = map(int,input().split())
        # print((x,y))
