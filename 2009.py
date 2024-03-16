N = int(input())
M = [list(map(int,input().split())) for _ in range(N)]
Mu = [[0]*N for _ in range(N)]

def obtener_vecinos_diagonales(i, j):
    vecinos = []
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        ni, nj = i + dx, j + dy
        if 0 <= ni < N and 0 <= nj < N:
            vecinos.append(M[ni][nj])
    return vecinos

for i in range(N):
    for j in range(N):
        Mu[i][j]=max(obtener_vecinos_diagonales(i, j))
        
for i in range(N):
    print(*Mu[i])