def dijkstra(Nodos, start, end, banned = -1):
    queue = [(0, start)]
    visited = {banned,}
    while queue:
        cost, node = queue.pop(0)
        if node == end:
            return start, end, cost
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in Nodos[node]:
            if neighbor in visited:
                continue
            queue.append((cost + weight, neighbor))
    return -1,-1,-1

N, M = map(int,input().split())
P, G = map(int,input().split())
Nodos = {i+1:set() for i in range(N)}
for _ in range(M):
    U,V,D = map(int,input().split())
    Nodos[U].add((V,D))
    Nodos[V].add((U,D))
_, _, costa = dijkstra(Nodos, P, G)
sw=False
for i in range(1,N+1):
    start, end, costb = dijkstra(Nodos, G, i, P)
    start, end, costc = dijkstra(Nodos, P, i, G)
    if costa==costb and costc>costa+costb:
        sw=True
        print(end, end=" ")
if not sw:
    print('*')

