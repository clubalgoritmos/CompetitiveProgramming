# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=228
## https://jv.umsa.bo/oj/problem.php?id=2640
#    Copiado al portapapeles
#  Michi Tenis
#  Enviar
#  Estado
#  Descripción
#    Amborgueso y Milaneso están organizando un reencuentro con amigos, y entre las actividades planificadas destaca un torneo de tenis de mesa. Un grupo de $n$ gatos entusiastas espera ansioso su turno para participar en este emocionante torneo.
#    La dinámica del torneo es simple: los dos primeros gatos en la fila juegan un partido de tenis de mesa. El ganador permanece en la cancha para enfrentar al siguiente gato de la fila, mientras que el perdedor se reincorpora al final de la fila. Este ciclo continúa hasta que un jugador logra ganar $k$ partidos consecutivos, asegurándose así la distinción de campeón.
#    Cada participante tiene un nivel de habilidad diferente, representado por su "poder" en el juego. En cada enfrentamiento, la victoria está garantizada para el jugador con el mayor poder. La pregunta es simple: ¿quién será el afortunado ganador que recibirá un premio en forma de Wiskas?
#   Entrada
#    La primera línea de entrada consistirá en un número t $(1 \leq t \leq 50)$ - cantidad de casos de entrada.
#    Luego las siguientes $t$ líneas consistirán en 2 líneas, la primera línea consistirá en 2 valores $n$ y $k$ $(2 \leq n \leq 500, 2 \leq k \leq 10^{12})$: el número de jugadores gatos y el número de victorias requeridas.La segunda línea consistirá en $n$ números enteros $a_1, a_2,...,a_n (1 \leq a_i \leq n)$ —  poderes de jugador. Se garantiza que esta línea contiene una permutación válida, es decir, todos los $a_i$ son $distintos$.
#   Salida
#    Para cada caso imprimir el poder el jugador que ganó.
#   Ejemplo Entrada
#    42 21 24 23 1 2 46 26 5 3 1 2 42 100000000002 1
#   Ejemplo Salida
#    2362
#   Ayuda
#    Juegos del segundo caso:
#    Jugador con poder 3 jugó con jugador con poder 1. Jugador con poder 3 ganó. Entonces jugador con poder 1 se va al final de la línea.
#    Jugador con poder 3 jugó con jugador con poder 2. Jugador con poder 3 ganó. Además ganó dos veces seguidas Entonces jugador con poder 3 se convierte en el ganador.

