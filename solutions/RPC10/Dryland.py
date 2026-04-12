a, b = map(int, input().split())
m = [input().strip() for _ in range(a)]

def rec(h):
    p = []
    ma = 0
    h.append(0)
    for i, x in enumerate(h):
        while p and h[p[-1]] >= x:
            al = h[p.pop()]
            an = i if not p else i - p[-1] - 1
            ma = max(ma, al * an)
        p.append(i)
    h.pop()
    return ma

h = [0] * b
ma = 0
for i in range(a):
    for j in range(b):
        if m[i][j] == '1':
            h[j] += 1
        else:
            h[j] = 0
    ma = max(ma, rec(h))

print(ma)