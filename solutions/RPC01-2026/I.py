N = int(input())
last = int(input())
C = [last]
for _ in range(N-1):
    a = int(input())+last
    C.append(a)
    last = a

for _ in range(int(input())):
    a,b,c = input().split()
    b,c=int(b),int(c)
    if a == "R":
        if b == 1:
            print(C[c-1])
        else:
            print(C[c-1]-C[b-2])
    if a == "U":
        for i in range(b-1,N):
            C[i]+=c
    