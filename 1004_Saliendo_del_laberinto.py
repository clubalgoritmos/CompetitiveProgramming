# https://jv.umsa.bo/oj/problem.php?id=1004
#  Saliendo del laberinto
#  Enviar
#  Estado
#  Descripción
#    Pepe tiene un problema, se encuentra en un laberinto y quiere salir de el, pero ese no es su único conflicto, ya que algunos laberintos no tienen un camino a la salida, así es que Pepe debe abrirse camino rompiendo algunas paredes, pero como necesita salir rápido quiere romper el menor numero de paredes.
#    Ayuda a Pepe diciéndole el numero mínimo de paredes a derrumbar, si hay un camino entre la posición de Pepe y la salida imprimir 0 , si no hay un camino imprimir el numero de paredes a derrumbar.
#    Nota: Pepe solo puede moverse hacia arriba, abajo, derecha e izquierda.
#   Entrada
#    La entrada cociste en T casos de entrada, cada caso comienza con dos enteros N, M  el tamaño del laberinto $( 2 <= N,M <= 100 ). Seguido del laberinto que es una matriz de tamaño N x M (la esquina superior izquierda en 0,0) que contiene los caracteres:
#    "#"   : Pared
#    "."   : Espacio libre
#    Tambien se le dara la coordenada (X1, Y1) donde esta Pepe y la coordenada ( X2, Y2) donde esta la salida. Se garantiza que la salida y en la posicion de Pepe siempre se encuentra el caracter "."
#   Salida
#    Por cada caso de entrada imprimir en una linea “Laberinto #X: ” (X es el numero de laberinto) seguido de la respuesta.
#   Ejemplo Entrada
#    25 5.#....#.#..#.#..#.#....#.0 04 44 5.#.#..#.#..#.#..#.#.0 00 4
#   Ejemplo Salida
#    Laberinto #1: 0Laberinto #2: 2
#   Ayuda
#    Fijate si debes ir izquierda o derecha, arriba o abajo para llegar al punto destino y tomala
#    Desde el punto de inicio signado (x1, y1) recorre filas, columnas puede ser de arriba o abajo, izquierda o derecha, dependiendo del (x2, y2) a donde se pida llegar. Una vez que no exista movimiento hacia el lado que debes ir rompe un muro pero mientras exista camino no lo hagas

from collections import deque

def funcion(n, m, laberinto, x1, y1, x2, y2):
    dist = [[float('inf')]*m for _ in range(n)]
    dist[x1][y1] = 0
    queue = deque([(x1, y1)])

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                cost = dist[x][y] + (laberinto[nx][ny] == "#")
                if cost < dist[nx][ny]:
                    dist[nx][ny] = cost
                    if laberinto[nx][ny] == "#":
                        queue.append((nx, ny))
                    else:
                        queue.appendleft((nx, ny))

    return dist[x2][y2] if dist[x2][y2] != float('inf') else -1

for _ in range(int(input())):
    n, m = map(int, input().split())
    laberinto = [list(input()) for _ in range(n)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print(f"Laberinto #{_+1}: {funcion(n, m, laberinto, x1, y1, x2, y2)}")