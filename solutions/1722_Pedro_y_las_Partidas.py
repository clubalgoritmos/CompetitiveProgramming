# https://jv.umsa.bo/oj/problem.php?id=1722
#  Pedro y las Partidas
#  Enviar
#  Estado
#  Descripción
#    Pedro y Juan están jugando partidas de 3 en raya al mejor de N.
#    Debido a que les da pereza escribir el resultadao de cada partida en un papel, quieren tener un programa en el que se introduzca el resultado de cada partida y una vez registradas todas, responda quién es el jugador ganador.
#    Ayúdales.
#   Entrada
#    Se te dará un número $N$ que representa el número de partidas que se jugarán.
#    En la siguiente línea, s e introducirán $N$ números, uno por línea, que pueden ser $1$ o $2$, que registra cuál de ambos jugadores ganó la respectiva partida.
#   Salida
#    La salida debe ser el texto "Gana el jugador 1!" o "Gana el jugador 2!", sin comillas, dependiendo de quién gane más partidas. Se garantiza que no hay empate.
#   Ejemplo Entrada
#    522121
#   Ejemplo Salida
#    Gana el jugador 2!
#   Ayuda

# Pedro y las partidas

partidas = int(input())
datos = []
for i in range(partidas):
    datos.append(input())
if datos.count("2") > datos.count("1"):
    print("Gana el jugador 2!")
else:
    print("Gana el jugador 1!")