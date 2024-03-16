n, m, k = map(int, input().split())
m-=1
a = list(map(int, input().split()))
left = next((i for i in range(m-1, -1, -1) if a[i] <= k and a[i]!=0), float('inf'))
right = next((i for i in range(m+1, len(a), 1) if a[i] <= k and a[i]!=0), float('inf'))
print((min(abs(left-m),abs(right-m)))*10)