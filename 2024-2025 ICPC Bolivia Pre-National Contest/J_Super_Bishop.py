from math import gcd
def solve():
    n, m = map(int, input().split())
    if gcd(n, m) == 1:
        print(0)
        return
    M = [[0] * m for _ in range(n)]
    x, y = 0, 0
    dx, dy = 1, 1
    M[x][y] = 1
    visited = 1
    while True:
        nx, ny = x + dx, y + dy
        if nx >= n or nx < 0:
            dx = -dx
            nx = x + dx
        if ny >= m or ny < 0:
            dy = -dy
            ny = y + dy
        if M[nx][ny] == 0:
            visited += 1
        x, y = nx, ny
        M[x][y] = 1
        if visited == n * m or (x == 0 and y == 0 and visited > 1):
            break
    print(n*m - visited)

while True:
    try:
        solve()
    except EOFError:
        break