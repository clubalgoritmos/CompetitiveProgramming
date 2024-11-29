import heapq

n = int(input())
a = list(map(int, input().split()))

if sum(a) != 2*n - 1:
    print(-1)
else:
    h = [(-x, i) for i, x in enumerate(a, start=1)]
    heapq.heapify(h)
    
    e = []
    while h:
        x, i = heapq.heappop(h)
        x = -x
        for _ in range(1, x):
            if h:
                nx, ni = heapq.heappop(h)
                nx = -(nx + 1)
                if nx != 0:
                    heapq.heappush(h, (nx, ni))
                e.append((i, ni))
            else:
                break
    
    e.sort(key=lambda x: (x[1], x[0]))
    
    print(len(e))
    for u, v in e:
        print(u, v)