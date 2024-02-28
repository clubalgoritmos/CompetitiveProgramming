from collections import deque

for _ in range(int(input())):
    N, M = (int(x) for x in input().split())
    graph = {i:set() for i in range(1,N+1)}
    for _ in range(M):
        u, v = (int(x) for x in input().split())
        graph[u].add(v)
        graph[v].add(u)
    X,Y = (int(x) for x in input().split())
    def bfs(graph, start):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                queue.extend(graph[node] - visited)
        return visited
    if Y in bfs(graph, X):
        print("SI")
    else:
        print("NO")
        