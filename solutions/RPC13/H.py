n = int(input())
dc = {i:0 for i in range(1,51)}
for _ in range(n*10):
    for i in map(int, input().split()):
        dc[i] += 1


print(*sorted([k for k, v in dc.items() if v > 2*n]) or [-1])
