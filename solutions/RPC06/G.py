class Graph:
    def __init__(self, N):
        self.adj = [[] for _ in range(N + 1)]
        self.mu_mc = (0, 0)
        self.N = N

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, n, p):
        N = self.N
        adj = self.adj
        ss = 1
        local_max = 0
        local_count = 0
        for c in adj[n]:
            if c != p:
                sz = self.dfs(c, n)
                eu = sz * (N - sz)
                if eu > local_max:
                    local_max = eu
                    local_count = 1
                elif eu == local_max:
                    local_count += 1
                ss += sz
        if local_max > self.mu_mc[0]:
            self.mu_mc = (local_max, local_count)
        elif local_max == self.mu_mc[0]:
            self.mu_mc = (self.mu_mc[0], self.mu_mc[1] + local_count)
        return ss

def main():
    N = int(input())
    graph = Graph(N)
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    graph.dfs(1, -1)
    print(graph.mu_mc[0], graph.mu_mc[1])

if __name__ == "__main__":
    main()