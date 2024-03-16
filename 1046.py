while True:
    try:
        N = int(input())
        A,B,C = [],[],[]
        for i in range(N):
            x,n = map(int,input().split())
            if x==1:
                A.append(n)
            else:
                B.append(n)
        if all(a==b for a,b in zip(A,B)):
            C.append("queue")
        if all(a==b for a,b in zip(A,reversed(B))): 
            C.append("stack")
        if all(a==b for a,b in zip(sorted(A,reverse=True),sorted(B,reverse=True))): 
            C.append("priority queue")
        print(C)
    except EOFError::
        break