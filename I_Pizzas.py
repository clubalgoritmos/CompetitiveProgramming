#Solucion
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.size = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
                self.size[rootX] += self.size[rootY]

MOD = 10**9 + 7

n, m = map(int, input().split())
uf = UnionFind(n + 1) 

for _ in range(m):
    a, b = map(int, input().split())
    uf.union(a, b)

product = 1
seen = set()
for i in range(1, n + 1):
    root = uf.find(i)
    if root not in seen:
        product = (product * uf.size[root]) % MOD
        seen.add(root)

print(product)