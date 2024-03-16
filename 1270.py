for _ in range(int(input())):
    N = int(input())
    A = []
    while N>0:
        if N-2>=0:
            A.append(8)
            N-=2
        elif N-1>=0:
            A.append(0)
            N-=1
        else:
            break
    if A==[]:
        A=[1]
    A.sort()
    bo = False
    for i,a in enumerate(A):
        if a!=0:
            bo = True
        if not bo and a==0 and len(A)!=1:
            A[i]=4
    print(*A,sep="") 