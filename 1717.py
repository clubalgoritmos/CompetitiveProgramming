#no funciona
for _ in range(int(input())):
    a,b = input().split()
    s=0
    for i, x in enumerate(zip(a,b)):
        ai,bi=map(int,x)
        u = abs(ai-bi)
        if u==0: u=1
        s+=u
    print(s)