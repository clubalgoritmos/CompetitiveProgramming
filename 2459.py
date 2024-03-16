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