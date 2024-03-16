while True:
    try:
        n = int(input())
        a = sorted(map(int,input().split()))
        st = set(a)
        if len(st)%2==0 and :
            print(-1)
            continue
        print(a[n//2])
    except EOFError:
        break