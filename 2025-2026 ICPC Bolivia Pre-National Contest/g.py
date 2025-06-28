n, k = map(int,input().split())
A = [int(i) for i in input().split()]
sumA = sum(A)
B = [1 for ai in A if (sumA-ai)%k==0]

print(sum(B),end="")
