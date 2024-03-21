# https://jv.umsa.bo/oj/problem.php?cid=2575&pid=6
## https://jv.umsa.bo/oj/problem.php?id=1944
#  Recorrido de Mac Demarco
#  Estado
#  Descripción
#    Mac Demarco se encuentra en la posicion en la esquina superior izquierda y quiere llegar a la esquina inferior derecha, en cada posicion entre su origen y destino existe un coste que se suma al recorrido si se pasa por ahi. Halle el minimo coste posible para llegar a su destino incluyendo el coste del origen y del destino.
#    En el ejemplo del grafico se puede ver claramente que la respuesta es 24.
#   Entrada
#    Varios casos de prueba T, La primera linea es un numero positivo que define el numero de filas N, luego separados por un salto de linea un M que represta el tamaño de las columnas.Donde 1<= N,M <=999.
#    Seguido de N x M enteros positivos que seran entre el 0 y el 9 que representaran el coste de cada posición.
#    posición
#    posición
#   Salida
#    Por cada caso de prueba imprima la respuesta correspondiente.
#   Ejemplo Entrada
#    3450 3 1 2 97 3 4 9 91 7 5 5 32 3 4 2 5160 1 2 3 4 5560 9 9 0 0 00 9 0 0 9 00 9 0 9 9 00 0 0 9 9 09 9 9 9 9 0
#   Ejemplo Salida
#    24150
#   Ayuda
for _ in range(int(input())):
    N = int(input()) #fila
    M = int(input()) #columna
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    dp = [[0]*M for _ in range(N)]
    dp[0][0] = grid[0][0]
    
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, M):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    print(dp[N-1][M-1],dp)