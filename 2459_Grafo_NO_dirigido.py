# https://jv.umsa.bo/oj/problem.php?cid=2567&pid=4
#  Grafo NO dirigido
#  Estado
#  Descripción
#    Un grafo NO dirigido, es un conjunto de nodos interconectados entre sí, de tal manera que se puede llegar de una NODO a otro NODO, simplemente siguiendo las líneas de conexión, ya sea de izquierda a derecha como de derecha a izquierda. A continuación, se muestran dos grafos.
#    Un grafo NO dirigido, es un conjunto de nodos interconectados entre sí, de tal manera que se puede llegar de una NODO a otro NODO, simplemente siguiendo las líneas de conexión, ya sea de izquierda a derecha como de derecha a izquierda. A continuación, se muestran dos grafos.
#    Un grafo NO dirigido, es un conjunto de nodos interconectados entre sí, de tal manera que se puede llegar de una NODO a otro NODO, simplemente siguiendo las líneas de conexión, ya sea de izquierda a derecha como de derecha a izquierda. A continuación, se muestran dos grafos.
#    El primer grafo tiene 7 nodos, y como podrás apreciar en la imagen, todos ellos están interconectados. Por tanto, es posible llegar desde cualquier nodo a cualquier nodo.
#    El primer grafo tiene 7 nodos, y como podrás apreciar en la imagen, todos ellos están interconectados. Por tanto, es posible llegar desde cualquier nodo a cualquier nodo.
#    El primer grafo tiene 7 nodos, y como podrás apreciar en la imagen, todos ellos están interconectados. Por tanto, es posible llegar desde cualquier nodo a cualquier nodo.
#    El segundo grafo tiene 8 nodos, y está organizado en 3 grupos. El primer grupo esta conformado por los nodos 1, 2 y 3. El segundo grupo por los nodos 4 y 5. El tercer grupo por los nodos 6, 7 y 8. Como podrás observar, NO es posible llegar del nodo 1 al nodo 7, por ejemplo.
#    El segundo grafo tiene 8 nodos, y está organizado en 3 grupos. El primer grupo esta conformado por los nodos 1, 2 y 3. El segundo grupo por los nodos 4 y 5. El tercer grupo por los nodos 6, 7 y 8. Como podrás observar, NO es posible llegar del nodo 1 al nodo 7, por ejemplo.
#    El segundo grafo tiene 8 nodos, y está organizado en 3 grupos. El primer grupo esta conformado por los nodos 1, 2 y 3. El segundo grupo por los nodos 4 y 5. El tercer grupo por los nodos 6, 7 y 8. Como podrás observar, NO es posible llegar del nodo 1 al nodo 7, por ejemplo.
#   Entrada
#    La primera línea contiene tres valores M, N y C. Donde M es el número de nodos que contiene el grafo no dirigido. N es el número de entradas que describen sus interconexiones. C es el número de casos de prueba, indicando el nodo de partida y el nodo de llegada.
#    La primera línea contiene tres valores M, N y C. Donde M es el número de nodos que contiene el grafo no dirigido. N es el número de entradas que describen sus interconexiones. C es el número de casos de prueba, indicando el nodo de partida y el nodo de llegada.
#    En el caso del ejemplo, tiene 3 casos de prueba y se pide verificar si se puede llegar del nodo 1 al nodo 4, luego del nodo 1 al nodo 6 y finalmente si se puede llegar del nodo 3 al nodo 7.
#    En el caso del ejemplo, tiene 3 casos de prueba y se pide verificar si se puede llegar del nodo 1 al nodo 4, luego del nodo 1 al nodo 6 y finalmente si se puede llegar del nodo 3 al nodo 7.
#   Salida
#    Se imprimirá un valor cero o un valor uno, que indicará si cada caso de prueba, tiene una ruta desde el nodo de partida al nodo de llegada. En caso de que exista una ruta se imprimirá un valor uno (1), y si no hay conexión entre los nodos de referencia, se imprimirá el valor cero (0).
#    Se imprimirá un valor cero o un valor uno, que indicará si cada caso de prueba, tiene una ruta desde el nodo de partida al nodo de llegada. En caso de que exista una ruta se imprimirá un valor uno (1), y si no hay conexión entre los nodos de referencia, se imprimirá el valor cero (0).
#    En el caso del ejemplo, los 3 casos de prueba son factibles, por eso, es que se imprime un valor 1 por cada caso de prueba.
#    En el caso del ejemplo, los 3 casos de prueba son factibles, por eso, es que se imprime un valor 1 por cada caso de prueba.
#   Ejemplo Entrada
#    7 6 31 22 41 33 55 65 71 41 63 7
#   Ejemplo Salida
#    111
#   Ayuda

from collections import defaultdict

def dfs(v, visited, adj):
    visited[v] = True
    for i in adj[v]:
        if visited[i] == False:
            dfs(i, visited, adj)

M, N, C = map(int, input().split())
adj = defaultdict(list)

for _ in range(N):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for _ in range(C):
    x, y = map(int, input().split())
    visited = [False] * (M + 1)
    dfs(x, visited, adj)
    print(1 if visited[y] else 0)