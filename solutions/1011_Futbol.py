# https://jv.umsa.bo/oj/problem.php?id=1011
#  Futbol
#  Enviar
#  Estado
#  Descripción
#    Como es de conocimiento, el futbol es el deporte más jugado en el mundo.
#    El juego consiste de 2 equipos, cada uno de 11 jugadores y un balón.
#    Pepe amante del futbol armo un equipo para poder competir en el campeonato del barrio. Ahora el planea diferentes tácticas para poder ganar cada partido que les toque disputar.
#    Entre todas las tacitas que él tiene, una es:
#    Realizar pases precisos desde un jugador A a un jugador B pasando por diferentes jugadores del equipo, pero la condición es que al pasar el balón desde el jugador A al jugador B el recorrido del balón debe ser la distancia más corta posible.
#    Para que puedas localizar cada jugador en el campo, se te darán coordenadas x, y  para cada jugador
#   Entrada
#    La primera línea de entrada contiene un entero N, el número de jugadores en el equipo de pepe (N<=11), después de la primera línea se te dará N líneas cada una de 2 valores x,y (donde x, y son las coordenadas del jugador Ni  1<=i<=N )
#    A continuación se te dará un entero Q, el número de consultas. Cada Qi linea estará compuesta 2 enteros A,B (A!=B) (Donde A y B son los jugadores insertados anteriormente).
#   Salida
#    Para cada consulta debe imprimir la distancia que atravesó el balón desde el jugador A al jugador B (recondeado a 2 digitos despues de la coma decimal).
#   Ejemplo Entrada
#    40 00 10 31 131 21 31 4
#   Ejemplo Salida
#    1.003.001.41
#   Ayuda
#    2da div. 2012 UMSA

graph = {i:tuple(map(int,input().split())) for i in range(int(input()))}
for _ in range(int(input())):
    a, b = map(int, input().split())
    xa, ya = graph[a-1]
    xb, yb = graph[b-1]
    print(f"{((xa-xb)**2+(ya-yb)**2)**.5:.2f}")