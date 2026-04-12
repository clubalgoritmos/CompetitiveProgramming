n, m, r = map(int, input().split())

cities = []

for _ in range(m):
    u, v = map(int, input().split())
    cities.append((0, u, v))

for _ in range(r):
    u, v, c = map(int, input().split())
    cities.append((c, u, v))

cities.sort()
ant = [i for i in range(n + 1)]
rk = [0] * (n + 1)


def find(u):
    while ant[u] != u:
        ant[u] = ant[ant[u]]
        u = ant[u]
    return u


def union(u, v):
    u_root = find(u)
    v_root = find(v)
    if u_root == v_root:
        return False
    if rk[u_root] < rk[v_root]:
        ant[u_root] = v_root
    else:
        ant[v_root] = u_root
        if rk[u_root] == rk[v_root]:
            rk[u_root] += 1
    return True


cost = 0
count = 0

for c, u, v in cities:
    if union(u, v):
        cost += c
        count += 1
        if count == n - 1:
            break

print(cost)
