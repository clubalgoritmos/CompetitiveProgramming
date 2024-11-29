# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=220
## https://jv.umsa.bo/oj/problem.php?id=2556
#    Copiado al portapapeles
#  Portales al infinito
#  Enviar
#  Estado
#  Descripción
#    Estas jugando un videojuego con temática del espacio, tendrás monedas espaciales y también podrás moverte a través de portales por el espacio.
#    Considere los puntos $0,1,…,n$ en una recta numérica. Hay un portal ubicado en cada uno de los puntos $1, 2, …, n$. En el punto $i$, puedes hacer lo siguiente:
#    Mover a la izquierda una unidad: cuesta $1$ moneda.
#    Mover a la derecha una unidad: cuesta $1$ moneda.
#    Usar un portal en el punto $i$, si existe: cuesta $a_i$ monedas Como resultado, te teletransportas al punto $0$. Una vez que usas un portal, no puedes volver a usarlo.
#    Tienes $c$ monedas, y comienzas en el punto $0$. ¿Cuál es la mayor cantidad de portales que puedes usar?
#   Entrada
#    La primera línea contiene un entero $t$ $(1 \leq t \leq 1000)$, el número de casos de prueba.
#    La primera línea de cada caso de prueba contiene dos números enteros $n$ y $c$, $(1 \leq n \leq 2*10^5;1 \leq c \leq 10^9)$, la longitud del arreglo donde se encuentran los costes y el número de monedas que tienes respectivamente.
#    La siguiente línea contiene $n$ enteros separados por espacios $a_1$,$a_2$,…,$a_n$. $(1 \leq a_i \leq 10^9)$, los costes de uso de los portales.
#   Salida
#    Para cada caso de prueba, genere la cantidad máxima de portales que puedes usar.
#   Ejemplo Entrada
#    105 61 1 1 1 18 32100 52 13 6 9 4 100 351 154 54 3 2 15 92 3 1 4 15 82 3 1 4 14 32 3 4 14 95 4 3 32 147 55 600000000500000000 400000000 300000000 200000000 100000000
#   Ejemplo Salida
#    2201221112
#   Ayuda
#    En el primer caso de prueba, puedes moverte una unidad a la derecha, puedes usar el portal en el índice 1 y teletransportarte al punto 0, luego te mueves dos unidades a la derecha y usar el portal en el índice 2. Te quedas con 6−1−1−2−1 = 1 monedas entonces no tienes suficientes monedas para usar otro portal. Haz utilizado dos portales, por lo que la respuesta es dos.
#    En el segundo caso de prueba, vas cuatro unidades a la derecha y usas el portal para ir a 0, luego vas 6 unidades a la derecha y usas el portal en el índice 6 para ir a 0. El costo total será 4+6+6+4=20. Te quedas con 12 monedas, pero no es suficiente para llegar a cualquier otro portal y usarlo, por lo que la respuesta es 2.
#    En el tercer caso de prueba, no tienes suficientes monedas para usar ningún portal, por lo que la respuesta es cero.

