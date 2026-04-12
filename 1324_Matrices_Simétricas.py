# https://jv.umsa.bo/oj/problem.php?id=1324
#  Matrices Simétricas
#  Enviar
#  Estado
#  Descripción
#    Se define una matriz cuadrada como simétrica si luego de transponer las filas y columnasobtenemos la misma matriz, por ejemplo la matriz, siguiente es simétrica:
#    2 3
#    3 4
#   Entrada
#    La entrada consiste de varios casos de prueba, la primera línea contiene el número de casos deprueba $n < 1000$. Para cada caso de prueba la primera línea contiene la dimensión de la matriz$(2 \leq m \leq 100)$, seguidos de $m^2$ elementos.
#   Salida
#    Su programa debe determinar, para cada caso de prueba si la matriz es simétrica, mostrandola frase Simétrica o No simétrica según sea el caso.
#   Ejemplo Entrada
#    34-2 3 -9 63 -4 4 -6-9 4 6 36 -6 3 621 45 631 2 3 1 1 4 3 4 1
#   Ejemplo Salida
#    SimetricaNo simetricaNo simetrica
#   Ayuda
#    puede realizar la consulta en la misma matriz analizando las posiciones

for _  in range(int(input())):
    n = int(input())
    M = [list(map(int, input().split())) for _ in range(n)]
    sw = False
    for i in range(n):
        for j in range(i,n):
            if M[i][j] != M[j][i]:
                print("No simetrica")
                sw = True
                break
        if sw:
            break
    if not sw:
        print("Simetrica")