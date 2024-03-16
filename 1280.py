while True:
    try:
        n = int(input())
        A = sorted(map(int,input().split()))
        for i in range(1,n+1):
            try:
                if i!=A[i-1]: raise Exception
            except:
                print(i)
                break
    except EOFError:
        break