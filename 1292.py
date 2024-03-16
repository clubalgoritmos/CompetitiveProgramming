while True:
    try:
        n=int(input())
        print(sum(map(int, input().split())))
    except EOFError:
        break