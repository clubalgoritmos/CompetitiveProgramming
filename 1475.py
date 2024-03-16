N, a, b = map(int,input().split())
A = list(map(int,input().split()))
for i in range(abs(a-b)//2+1):
    A[a+i],A[b-i] = A[b-i],A[a+i]
for a in A:
    print(a)