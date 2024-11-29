# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=71
## https://jv.umsa.bo/oj/problem.php?id=1377
#    Copiado al portapapeles
#  Baja Prioridad
#  Enviar
#  Estado
#  Descripción
#    Valve, desarrolador de Dota 2, creó un nuevo sistema buscador de partidas en baja prioridad por equipo. Baja prioridad es un conjunto de personas horribles que abandonan partidas a menudo o tienen un comportamiento deplorable en juego, por esto y para castigarlos, se crearon una variedad de salas en las que deben esperar un cierto tiempo hasta que tengan oportunidad de tener una partida. El sistema de buscador de partida mueve equipos de una sala a otra cada minuto, por ejemplo, si se estubiera en la sala número i, el sistema te moverá a la sala número s[i] después de un minuto. Si hay dos o más equipos en una misma sala en un mismo tiempo entonces se crea un partida para que al fin puedan jugar. Tu trabajo es predecir cual es el primero minuto en el que dos o más equipos se encuentren, en el hipotético caso de que se pusiera a correr el sistema testeándolo con un hipotético conjunto de datos de prueba.
#   Entrada
#    La primer línea contiene un número natural n 1<=n<=10^5 que representa la cantidad de salas de espera. Las siguientes n líneas son números enteros s[1], s[2], s[3], ..., s[n] indicando que si se está en la sala i en el minuto t, entonces en el minuto t+1 se moverá instantáneamente a la sala número s[i]. Se garantiza que existirá por lo menos una sala "especial" tal que, no importando en que otra sala se encuentre un equipo, en algún momento llegará a dicha sala "especial". A continuación en la sigueinte línea se le da un natural m 1<=m<=10^5 indicando la cantidad de equipos. Las siguientes y últimas m líneas contienen dos números, v y t, 1<=v<=n, 1<=t<=10^15, la sala destinada a uno de los equipos y el minuto en el que "entrará" a dicha la sala.
#   Salida
#    Imprimir el mínuto en el que dos o más equipos se encuentran y si nunca sucede esto imprimir "-1" sin comillas.
#   Ejemplo Entrada
#    114 1 1 5 1 5 6 6 8 8 10311 02 49 0
#   Ejemplo Salida
#    5
#   Ayuda

