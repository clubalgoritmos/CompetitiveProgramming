import heapq

N,M,K = map(int, input().split())

dicts = {}
for ni in range(N):
    dicts[ni + 1] = set()

for mi in range(M):
    u,v,w = map(int, input().split())
    dicts[u].add((v, w))
    dicts[v].add((u, w))

dist = {i: float('inf') for i in dicts}
prev = {i: None for i in dicts}
dist[1] = 0

heap = [(0, 1)]
while heap:
    d, node = heapq.heappop(heap)
    if d != dist[node]:
        continue
    if node == N:
        break
    for neighbor, w in dicts[node]:
        nd = d + w
        if nd < dist[neighbor]:
            dist[neighbor] = nd
            prev[neighbor] = node
            heapq.heappush(heap, (nd, neighbor))
            
if dist[N] == float('inf') or dist[N] > K:
    print("NO")
else:
    print("SI")