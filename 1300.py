while True:
    try:
        N = int(input())
        A = list(map(int,input().split()))
        print(A.count(A[-1]))
    except EOFError:
        break