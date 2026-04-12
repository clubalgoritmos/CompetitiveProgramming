n = int(input())
d = list(map(int, input().split()))

a = d[0]//3
b = d[1]-2*a
c = d[-1]//3
print(a,b,c)
