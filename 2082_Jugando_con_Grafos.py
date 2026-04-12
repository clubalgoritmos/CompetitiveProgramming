# https://jv.umsa.bo/oj/problem.php?id=2082
#  Jugando con Grafos
#  Enviar
#  Estado
#  Descripción
#    Un grafo es un conjunto de vértices (tambien llamados nodos) y arcos (tambien llamados conexiones), usualmente se usan grafos para representar conexiones de internet, conexiones entre ciudades o incluso redes de distribución de agua o electricidad.
#    Para representar un grafo en programación usualmente se utilizan dos representaciones. Una matriz de adyacencia y una lista de adyacencia. Tu tarea ahora es que dad una matriz de adyacencia de un grafo, debes generar la lista de adyacencia.
#    Para un mayor nivel de comprensión puedes observar la imagen superior, la parte (a) es un grafo, la parte (b) es la lista de adyacencia y la parte (c) es la matriz de adyacencia.
#   Entrada
#    La entrada contiene solo un caso de prueba. La primera linea de entrada contiene a N, que representan el número de Nodos del grafo ( $2 \leq N \leq 1000$). Luego siguen N lineas cada una con N números que representa la matriz de adyacencia.
#   Salida
#    Debes imprimir la lista de adyacencia que se genera a partir de la matriz de adyacencia, como se muestra en el ejemplo.
#   Ejemplo Entrada
#    50 1 0 0 11 0 1 1 10 1 0 1 00 1 1 0 11 1 0 1 0
#   Ejemplo Salida
#    2 5 1 3 4 5 2 4 2 3 5 1 2 4
#   Ayuda

N = int(input())
M = [list(map(int,input().split())) for _ in range(N)]
graph = {k:set() for k in range(1,N+1)}
for i in range(N):
    for j in range(N):
        if M[i][j] == 1:
            graph[i+1].add(j+1)
            graph[j+1].add(i+1)
for k in graph:
    for i in graph[k]:
        print(i,end=" ")
    print()