N=int(input())
a,b,c = 1,1,1
for i in range(N):
    c=a+b
    a,b = b,c
print(a)