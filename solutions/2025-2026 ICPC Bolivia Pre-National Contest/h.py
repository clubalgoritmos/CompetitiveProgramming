import sys

input = sys.stdin.readline


class Fenw:
    def __init__(self, n):
        self.n = n
        self.fw = [0] * (n + 1)

    def update(self, i, diff):
        while i <= self.n:
            self.fw[i] += diff
            i += i & -i

    def query(self, i):
        s = 0
        while i:
            s += self.fw[i]
            i -= i & -i
        return s


def lower_bound(arr, value):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < value:
            lo = mid + 1
        else:
            hi = mid
    return lo


N, Q = map(int, input().split())
points = []
lp_list = []
for _ in range(N):
    x, y = map(int, input().split())
    lp = x - y
    rp = x + y
    points.append((lp, rp))
    lp_list.append(lp)

queries = []
query_lp = []
for idx in range(Q):
    l, r = map(int, input().split())
    queries.append((l, r, idx))
    query_lp.append(l)

all_lp = sorted(set(lp_list + query_lp))
lp_to_idx = {val: i + 1 for i, val in enumerate(all_lp)}
size = len(all_lp)

points.sort(key=lambda pr: pr[1])
queries.sort(key=lambda q: q[1])

fenw = Fenw(size)
ans = [0] * Q
pt_idx = 0
n_points = len(points)

for l, r, q_idx in queries:
    while pt_idx < n_points and points[pt_idx][1] <= r:
        lp_val = points[pt_idx][0]
        fenw.update(lp_to_idx[lp_val], 1)
        pt_idx += 1
    pos = lower_bound(all_lp, l)
    if pos == len(all_lp):
        ans[q_idx] = 0
    else:
        pos += 1
        total = fenw.query(size)
        count = total - fenw.query(pos - 1)
        ans[q_idx] = count

print(" ".join(map(str, ans)))
