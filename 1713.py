while True:
    try:
        N = int(input())
        S = 0
        for _ in range(N):
            S+=int(input())
        print(S)
    except EOFError:
        break