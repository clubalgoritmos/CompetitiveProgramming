# https://jv.umsa.bo/oj/problem.php?id=2009
#  Encriptando la Matriz
#  Enviar
#  Estado
#  Descripción
#    La empresa de seguros patito lo contrato para diseñar un software de encriptación para mantener seguro el dato de los clientes, se trata de lo siguiente:
#    Se le dará una matriz A de tamaño NxN llena de números la cual usted debe generar otra matriz B, en las posiciones x,y de la matriz B debe poner el mayor numero de los valores de las esquinas de la posición x,y de la matriz A es decir:
#    Las posiciones que no tengan todas sus esquinas, calcular con las esquinas que se tiene.
#   Entrada
#    Como datos de entrada se le dará un N donde(2<=N<=100) seguido de la matriz de enteros NxN.
#   Salida
#    La salida debe ser una matriz de NxN (Los elementos de cada fila deben estar separados por espacios, un espacio entre cada dos elementos).
#   Ejemplo Entrada
#    45 8 4 211 15 80 256 58 94 2056 53 21 24
#   Ejemplo Salida
#    15 80 25 8058 94 58 9453 80 53 8058 94 58 94
#   Ayuda

N = int(input())
M = [list(map(int,input().split())) for _ in range(N)]
Mu = [[0]*N for _ in range(N)]

def obtener_vecinos_diagonales(i, j):
    vecinos = []
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        ni, nj = i + dx, j + dy
        if 0 <= ni < N and 0 <= nj < N:
            vecinos.append(M[ni][nj])
    return vecinos

for i in range(N):
    for j in range(N):
        Mu[i][j]=max(obtener_vecinos_diagonales(i, j))
        
for i in range(N):
    print(*Mu[i])