# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=148
## https://jv.umsa.bo/oj/problem.php?id=1814
#    Copiado al portapapeles
#  Laberintos
#  Enviar
#  Estado
#  Descripción
#    José es un desarrollador de video juegos que entró a trabajar recientemente en la empresa “Carlos Pato” y le designaron una  tarea en la que tiene que añadirle nuevas misiones al juego “Zelda Breath of the Wild”.
#    La idea de José es añadir laberintos para que el juego tenga más complejidad.
#    En el juego, Link está dentro de una bestia divina, donde dentro de sí hay muchos laberintos.
#    Cada laberinto construido dentro de la bestia divina está formado por habitaciones conectadas por pasillos. Cada corredor conecta un par diferente de habitaciones distintas y puede atravesarse en ambas direcciones.
#    En este momento a José se le ocurren varios desafíos como por ejemplo, que la misión de Link consista en encontrar un camino simple desde una sala de inicio hasta el final de la habitación en un laberinto. Un camino simple es una secuencia de habitaciones distintas de modo que cada par de habitaciones en la secuencia están conectadas por un corredor. En este caso, la primera sala de la secuencia debe ser la sala de inicio, y la última sala de la secuencia debe ser la sala final. José piensa que un desafío es bueno cuando, entre las rutas tomadas desde la sala de inicio hasta la sala final, exactamente una de ellas es un camino simple.
#    ¿Puedes ayudar a José a elegir un desafío que complazca a la empresa “carlos pato”?
#    Para hacerlo, escriba un programa que proporcione la descripción de un laberinto y una lista de consultas que definan el salas de inicio y final, determina para cada consulta si esa elección de salas es un buen desafío o no.
#   Entrada
#    Cada caso de entrada tiene varias líneas. La primera línea contiene tres enteros R, C y Q representando respectivamente el número de cuartos en el laberinto (2 ≤ R ≤ 10^4 ), el número de pasillos (1 ≤ C ≤ 10^5 ), y el número de preguntas (1 ≤ Q ≤ 1000). Las habitaciones están identificadas por diferentes enteros desde 1 hasta R. Las siguientes C líneas describen el pasillo utilizando los enteros A y B, indicando que es el pasillo que conecta a A y a B (1 ≤ A < B ≤ R). Después de eso, las siguientes Q líneas describen las preguntas utilizando dos distintos enteros S y T indicando respectivamente el comienzo y el final de las habitaciones en el desafío (1 ≤ S < T ≤ R). Puedes suponer que dentro de cada caso de prueba hay como máximo un corredor que conecta cada par de habitaciones, y no hay dos consultas iguales.
#    El último caso de prueba es seguido por una línea que contiene tres ceros.
#   Salida
#    Por cada caso de salida imprimir Q+1 lineas. En la i-esima línea imprimir la respuesta de la i-esima pregunta. Si las habitaciones son un buen desafio imprimir “Y”. De lo contrario imprimir “N”. Imprimir una linea que contenga un caracter “-” al final de cada caso de prueba.
#   Ejemplo Entrada
#    6 5 31 22 3 2 4 2 5 4 5 1 3 1 5 2 6 0 0 0
#   Ejemplo Salida
#    YNN-
#   Ayuda

