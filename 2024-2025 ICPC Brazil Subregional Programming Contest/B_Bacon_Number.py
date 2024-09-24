from collections import deque, defaultdict

n, m = map(int, input().split())
common = defaultdict(lambda: defaultdict(lambda: -1))
has = defaultdict(set)
reach = defaultdict(lambda: defaultdict(bool))
par = defaultdict(lambda: defaultdict(lambda: -1))
adj = defaultdict(set)
g = defaultdict(set)

for i in range(n):
    line = list(map(int, input().split()))
    sz = line[0]
    for x in line[1:]:
        x -= 1
        has[i].add(x)
        adj[i].add(x)

def get(i, j):
    if len(adj[i]) > len(adj[j]):
        i, j = j, i
    for k in adj[i]:
        if k in adj[j]:
            return k
    return -1

for i in range(n):
    for j in range(i, n):
        curr = get(i, j)
        common[i][j] = curr
        common[j][i] = curr
        if curr != -1:
            g[i].add(j)
            g[j].add(i)

for ini in range(n):
    reach[ini][ini] = True
    q = deque([ini])
    while q:
        x = q.popleft()
        for y in range(n):
            if not reach[ini][y] and common[x][y] != -1:
                reach[ini][y] = True
                par[ini][y] = x
                q.append(y)

def solve(a, b):
    for i in range(n):
        if a in has[i]:
            for j in range(n):
                if reach[i][j] and b in has[j]:
                    ans = []
                    x = j
                    ans.append(b)
                    while True:
                        ans.append(x)
                        if x == i:
                            break
                        nxt = par[i][x]
                        ans.append(common[x][nxt])
                        x = nxt
                    ans.append(a)
                    ans.reverse()
                    print((len(ans) + 1) // 2)
                    print(" ".join(map(lambda x: str(x + 1), ans)))
                    return
    print("-1")

q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    solve(a - 1, b - 1)