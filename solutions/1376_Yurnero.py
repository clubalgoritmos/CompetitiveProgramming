# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=70
## https://jv.umsa.bo/oj/problem.php?id=1376
#    Copiado al portapapeles
#  Yurnero
#  Enviar
#  Estado
#  Descripción
#    Yurnero Juggernaut es un héroe de Dota 2. El ataque más poderoso o "la sexta" de \textit{Yurnero} es \textit{Omnislash}, que le permite atacar por saltos a múltiples enemigos al rededor. Yurnero está rodeado de $n$ enemigos debilitados, es decir que están a un simple golpe de morir, y para evitar que todos huyan utilizará \textit{Omnislash}. Como todos saben, \textit{Omnislash} de \textit{Yurnero} salta de manera convexa, es decir, que inicia por algún enemigo golpeándolo, luego, salta directamente sobre otro haciendo lo mismo y así hasta que ya no pueda golpear a nadie más; todo esto ocurriendo instantáneamente. Lo importante es las coordenadas de cada enemigo al que haya saltado deben ser los vértices de algún polígono convexo y además esto se produce de manera aleatoria . Todos los enemigos están a punto de morir por lo cual \textit{Yurnero} no los golpeará dos veces y además es posible que el poder alcance a todos ellos no importando la distancia que deba saltar tanto al utilizar el poder como en el proceso. Derrotar enemigos te da una recompensa en oro, conociendo las coordenadas de los $n$ enemigos en el instante en el que \textit{Yurnero} utilizará \textit{Omnislash} ¿Cuál es la mayor ganancia en oro que este podría obtener con la mejor de las suertes y el mejor desempeño?
#   Entrada
#    La primera línea de entrada contiene un número natural $3\leq n \leq 40$, el número de enemigos cercanos a \textit{Yurnero}. Las siguientes $n$ líneas tienen tres números enteros cada una $0 \leq x_i,y_i \leq 1000000$, $0 \leq g_i \leq 1000000$, que representan la posición en el mapa $(x,y)$ del enemigo i-esimo y la ganancia en oro que obtendrá \textit{Yurnero} si lo asesina. Se garantiza que no existirán 3 o más puntos co-lineales, es decir que exista una línea que pase por los tres.
#   Salida
#    Imprimir la ganancia máxima en oro que \textit{Yurnero} podría obtener al utilizar \textit{Omnislash}.
#   Ejemplo Entrada
#    40 0 11 3 21 1 23 1 2
#   Ejemplo Salida
#    6
#   Ayuda

