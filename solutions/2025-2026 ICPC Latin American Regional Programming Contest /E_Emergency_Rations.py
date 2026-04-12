import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)
Q = int(data[0])
ops = data[1:]

vals = [abs(int(x)) for x in ops]

uniq = sorted(set(vals))
m = len(uniq)
pos = {v: i for i, v in enumerate(uniq)}

INF = 10**18


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        i += 1
        n = self.n
        bit = self.bit
        while i <= n:
            bit[i] += delta
            i += i & -i

    def sum(self, i):
        # sum [0..i]
        i += 1
        s = 0
        bit = self.bit
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        if r < l:
            return 0
        return self.sum(r) - (self.sum(l - 1) if l else 0)


class SegTree:
    def __init__(self, n, init):
        self.n0 = 1
        while self.n0 < n:
            self.n0 <<= 1
        self.size = self.n0
        self.minv = [INF] * (2 * self.n0)
        self.lazy = [0] * (2 * self.n0)

    def _apply(self, idx, val):
        self.minv[idx] += val
        self.lazy[idx] += val

    def _push(self, idx):
        v = self.lazy[idx]
        if v:
            self._apply(idx * 2, v)
            self._apply(idx * 2 + 1, v)
            self.lazy[idx] = 0

    def _pull(self, idx):
        self.minv[idx] = min(self.minv[idx * 2], self.minv[idx * 2 + 1])

    def range_add(self, l, r, val):

        if l > r:
            return
        self._range_add(1, 0, self.n0 - 1, l, r, val)

    def _range_add(self, idx, left, right, ql, qr, val):
        if ql <= left and right <= qr:
            self._apply(idx, val)
            return
        if right < ql or qr < left:
            return
        self._push(idx)
        mid = (left + right) // 2
        self._range_add(idx * 2, left, mid, ql, qr, val)
        self._range_add(idx * 2 + 1, mid + 1, right, ql, qr, val)
        self._pull(idx)

    def point_set(self, p, value):
        idx = 1
        left = 0
        right = self.n0 - 1
        path = []
        while left != right:
            path.append(idx)
            self._push(idx)
            mid = (left + right) // 2
            if p <= mid:
                idx = idx * 2
                right = mid
            else:
                idx = idx * 2 + 1
                left = mid + 1
        self.minv[idx] = value

        for i in reversed(path):
            self._pull(i)

    def query_min(self):
        return self.minv[1]


fenw = Fenwick(m)
seg = SegTree(m, INF)
counts = [0] * m
k = 0
out = []

for tok in ops:
    sign = tok[0]
    c = abs(int(tok))
    idx = pos[c]
    if sign == "+":

        k += 1
        counts[idx] += 1
        fenw.add(idx, 1)
        pref_after = fenw.sum(idx)
        seg.range_add(idx, m - 1, -1)

        seg.point_set(idx, uniq[idx] - pref_after)
    else:

        k -= 1
        counts[idx] -= 1
        fenw.add(idx, -1)
        pref_after = fenw.sum(idx)
        seg.range_add(idx, m - 1, +1)
        if counts[idx] > 0:
            seg.point_set(idx, uniq[idx] - pref_after)
        else:
            seg.point_set(idx, INF)
    if k == 0:
        out.append("0")
    else:
        mn = seg.query_min()

        ans = k + mn
        if ans > k:
            ans = k
        out.append(str(ans))

print(" ".join(out))
