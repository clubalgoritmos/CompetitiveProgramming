import sys

input = sys.stdin.readline

N = int(input())
ls = [tuple(map(int, input().split())) for _ in range(N)]

d = [abs(ls[i][0] - ls[i + 1][0]) + abs(ls[i][1] - ls[i + 1][1]) for i in range(N - 1)]

S = [0] * (N + 1)
for i in range(1, N):
    S[i + 1] = d[i - 1] - S[i]

INF = 10**30
lower, upper = -INF, INF

for i in range(1, N):
    si = S[i]
    di = d[i - 1]
    if i % 2 == 1:
        lower = max(lower, 1 - si)
        upper = min(upper, di - si - 1)
    else:
        lower = max(lower, si - di + 1)
        upper = min(upper, si - 1)

if N % 2 == 1:
    lower = max(lower, 1 - S[N])
else:
    upper = min(upper, S[N] - 1)

if lower <= upper:
    print(upper)
else:
    print(-1)
