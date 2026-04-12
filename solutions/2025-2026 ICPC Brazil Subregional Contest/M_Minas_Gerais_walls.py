import sys
input = sys.stdin.readline

N, K = map(int, input().split())
X = list(map(int, input().split()))

mn, mx = min(X), max(X) + K
rs = mn

while mn <= mx:
    md = (mn + mx) // 2

    df = [max(0, md - h) for h in X]
    if any(d > K for d in df):
        ps = False
    else:
        R = float('inf')
        mx_j = -1
        for j, d in enumerate(df, 1):
            if d > 0:
                R = min(R, j + K - d)
                mx_j = j
        if mx_j == -1:
            ps = True
        else:
            ps = (R >= mx_j)

    if ps:
        rs = md
        mn = md + 1
    else:
        mx = md - 1

print(rs)
