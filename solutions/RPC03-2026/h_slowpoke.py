import heapq
import sys


def main() -> None:
    input = sys.stdin.readline

    n, m, k, d, s, t = map(int, input().split())

    roads = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, l = map(int, input().split())
        roads[a].append((b, l))
        roads[b].append((a, l))

    continuous = set()
    for _ in range(k):
        a, b, c = map(int, input().split())
        continuous.add((a, b, c))

    inf = 10**18
    limit = d + 1
    dist = [[[inf] * (limit + 1) for _ in range(n + 1)] for _ in range(n + 1)]

    start_prev = 0
    dist[start_prev][s][0] = 0
    pq = [(0, start_prev, s, 0)]

    while pq:
        cost, prev, curr, run_len = heapq.heappop(pq)
        if cost != dist[prev][curr][run_len]:
            continue

        if curr == t:
            print(cost)
            return

        for nxt, weight in roads[curr]:
            if nxt == prev:
                continue

            if prev == 0:
                new_run = weight
            elif (prev, curr, nxt) in continuous:
                if run_len > d or run_len + weight > d:
                    continue
                new_run = run_len + weight
            else:
                new_run = weight

            if new_run > limit:
                new_run = limit

            new_cost = cost + weight
            if new_cost < dist[curr][nxt][new_run]:
                dist[curr][nxt][new_run] = new_cost
                heapq.heappush(pq, (new_cost, curr, nxt, new_run))

    print("impossible")


if __name__ == "__main__":
    main()
