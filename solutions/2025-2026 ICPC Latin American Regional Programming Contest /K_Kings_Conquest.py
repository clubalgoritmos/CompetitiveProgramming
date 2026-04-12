N, K = map(int, input().split())
board = [tuple(map(int, input().split())) for _ in range(N)]

rows = [r for r, c in board]
cols = [c for r, c in board]
rmin, rmax = min(rows), max(rows)
cmin, cmax = min(cols), max(cols)

R0 = rmax - rmin + 1
C0 = cmax - cmin + 1

# minimal moves to put some king exactly at any current corner
corners = [(rmin, cmin), (rmin, cmax), (rmax, cmin), (rmax, cmax)]
t_min = min(max(abs(r - cr), abs(c - cc)) for (r, c) in board for (cr, cc) in corners)

# Strategy 1: no diagonal synergy (allocate a moves to rows, K-a to cols)
# maximize f(a) = (R0 + a) * (C0 + K - a) over integer a in [0,K]
# continuous optimum a* = (K + C0 - R0) / 2
a_star = (K + C0 - R0) / 2.0
candidates = {0, K, int(a_star), int(a_star) + 1}
f_max = 0
for a in candidates:
    if 0 <= a <= K:
        f_max = max(f_max, (R0 + a) * (C0 + (K - a)))

# Strategy 2: create a corner using t_min moves, then use remaining moves diagonally
g = 0
if K >= t_min:
    rem = K - t_min
    g = (R0 + rem) * (C0 + rem)

print(max(f_max, g))