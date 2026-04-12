import heapq
import sys


def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    C = int(next(it))

    cost = [0] + [int(next(it)) for _ in range(N)]  # 1-indexado

    # Grafo
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u = int(next(it))
        v = int(next(it))
        d = int(next(it))
        if d <= C:  # ignorar carreteras imposibles
            adj[u].append((v, d))
            adj[v].append((u, d))

    S = int(next(it))
    T = int(next(it))

    # Dijkstra sobre estados: (costo, ciudad, combustible)
    INF = 10**18
    dist = [[INF] * (C + 1) for _ in range(N + 1)]
    dist[S][C] = 0

    pq = [(0, S, C)]  # (costo, ciudad, combustible)

    while pq:
        cur_cost, u, fuel = heapq.heappop(pq)

        if cur_cost > dist[u][fuel]:
            continue
        if u == T:
            print(cur_cost)
            return

        # 1) Repostar si existe estación
        if cost[u] != -1 and fuel < C:
            new_cost = cur_cost + cost[u]
            if new_cost < dist[u][C]:
                dist[u][C] = new_cost
                heapq.heappush(pq, (new_cost, u, C))

        # 2) Viajar a ciudad vecina si alcanza el combustible
        for v, d in adj[u]:
            if fuel >= d:
                new_fuel = fuel - d
                if cur_cost < dist[v][new_fuel]:
                    dist[v][new_fuel] = cur_cost
                    heapq.heappush(pq, (cur_cost, v, new_fuel))

    # Si no se pudo llegar
    print(-1)


if __name__ == "__main__":
    solve()
