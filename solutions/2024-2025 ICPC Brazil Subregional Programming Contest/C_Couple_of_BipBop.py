from math import gcd
from collections import defaultdict

def suffix_array(s):
    s.append(0)
    n = len(s)
    N = n + 1
    sa = list(range(n))
    ra = s[:]

    k = 1
    while k < n:
        nsa = [(ra[i], ra[(i + k) % n], i) for i in range(n)]
        nsa.sort()
        sa = [x[2] for x in nsa]
        nra = [0] * n
        for i in range(1, n):
            nra[sa[i]] = nra[sa[i - 1]]
            if nsa[i][:2] != nsa[i - 1][:2]:
                nra[sa[i]] += 1
        ra = nra
        if ra[sa[-1]] == n - 1:
            break
        k *= 2

    return sa[1:]

def kasai(s, sa):
    n = len(s)
    k = 0
    ra = [0] * n
    lcp = [0] * (n - 1)
    for i, suffix in enumerate(sa):
        ra[suffix] = i
    for i in range(n):
        if ra[i] == n - 1:
            k = 0
            continue
        j = sa[ra[i]-1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[ra[i]] = k
        if k:
            k -= 1
    return lcp

class RMQ:
    def __init__(self, v):
        self.n = len(v)
        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1
        self.m = [[(float('inf'), -1)] * (self.n + 1) for _ in range(self.log[self.n] + 1)]
        for i in range(self.n):
            self.m[0][i] = v[i]
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while i + (1 << j) <= self.n:
                self.m[j][i] = min(self.m[j - 1][i], self.m[j - 1][i + (1 << (j - 1))])
                i += 1
            j += 1

    def qry(self, a, b):
        j = self.log[b - a + 1]
        return min(self.m[j][a], self.m[j][b - (1 << j) + 1])[1]

def solve(a, b, l, rm):
    if a > b:
        return 0
    mid = rm.qry(a, b)
    tot = (mid - a + 1) * (b - mid + 1)
    tot *= l[mid][0]
    tot += solve(a, mid - 1, l, rm)
    tot += solve(mid + 1, b, l, rm)
    return tot

def main():
    n = int(input())
    v = list(map(int, input().split()))
    sa = suffix_array(v)
    lcp = kasai(v, sa)
    l = [(2 * lcp[i], i) for i in range(len(lcp))]
    sum_ = sum(range(1, n + 1))
    rm = RMQ(l)
    sum_ += solve(0, len(l) - 1, l, rm)
    tot = n * n
    g = gcd(sum_, tot)
    sum_ //= g
    tot //= g
    print(f"{sum_}/{tot}")

if __name__ == "__main__":
    main()