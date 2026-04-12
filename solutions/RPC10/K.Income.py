n = int(input())
m_n = sorted(map(int, input().split()), reverse=True)
s = sum(m_n)
mxd = 0.0
cs = 0

for k in range(1, n + 1):
    cs += m_n[k - 1]
    x = k / n * 100
    y = cs / s * 100
    df = y - x
    if df > mxd:
        mxd = df

print(f"{mxd:.6f}")
