N = int(input())
M = [list(map(int,input().split())) for _ in range(N)]
graph = {k:set() for k in range(1,N+1)}
for i in range(N):
    for j in range(N):
        if M[i][j] == 1:
            graph[i+1].add(j+1)
            graph[j+1].add(i+1)
for k in graph:
    for i in graph[k]:
        print(i,end=" ")
    print()