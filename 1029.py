while True:
    try:
        A = list(map(int,input().split()))
        s = 0
        i = 1
        while len(A)>0:
            a=max(A)
            s+=a*i
            i*=-1
            A.pop(A.index(a))
        print(abs(s))
    except EOFError:
        break