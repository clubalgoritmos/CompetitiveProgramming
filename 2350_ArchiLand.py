# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=198
## https://jv.umsa.bo/oj/problem.php?id=2350
#    Copiado al portapapeles
#  ArchiLand
#  Enviar
#  Estado
#  Descripción
#    Bienvenido a ArchiLand, un archipielago muy calido y florido en estas epocas del año, ¿Estas listo para relajarte?
#    Pues lastimosa tu eres el administrador y estas epocas del año son muy agetreadas para ti, es por eso que tu trabajo es poner puertos para barcos (denotado con el caracter #) para que los barcos lleguen a cada isla, es por eso que uno de los ingenieros te entrega un mapa, representado como una matriz de $n$ filas y $m$ columnas, donde el simbolo (.) simboliza el agua y el conjunto de simbolos (o) adyacentes representan una isla.
#    Es decir:
#    En este mapa, podemos ver 2 islas, entonces te piden que entregues un mapa donde pongas puertos en las orillas de cada isla en las cuatro direciones Este, Oeste, Norte, Sur sin importar que estas se superpongan .
#   Entrada
#    Una linea que contiene un entero $t$ (1 \le t \le 10) indicando el numero de casos de prueba
#    Por cada caso de prueba tenemos:
#    Una linea con 2 enteros $n,m (1 \le n,m \le 500) $ indicando las dimensiones del mapa
#    Luego siguen $n$ lineas con $m$ caracteres, donde el caracter $c_{i,j} ={o,.}$ donde $o = pedazo de la isla$, $. = mar$
#   Salida
#    Una matriz indicando el mapa solicitado acompañado de un salto de linea extra.
#   Ejemplo Entrada
#    25 5. . . . .. o o o .. o . o .. . . o .. . . . .5 5. o . . .o o o . .. . o . .. . o . .. . . . o
#   Ejemplo Salida
#    . # # # . # o o o # # o # o # . # # o # . . . # . # o # . . o o o # . # # o # . . # o # # . . # # o
#   Ayuda

