while True:
    try:
        a,b = map(int,input().split())
        while True:
            x = a+b//2
    except EOFError:
        break