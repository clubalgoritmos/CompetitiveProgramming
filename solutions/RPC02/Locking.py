n,m = map(int,input().split())

import heapq
import collections

graph = collections.defaultdict(list)

for _ in range(m):
    a,b = map(int,input().split())#es de b => a
    graph[b].append(a)
s=0
for nodo in range(1,n+1):
    if not graph[nodo]:
        s+=1
if s==0:
    s=2
print(s)