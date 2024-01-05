for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    sw=False
    for i in range(n):
        for j in range(i+1, n+1):
            x = arr[i:j]
            if x == x[::-1] and len(x) > 2:
                print('TIENE')
                sw=True 
                break
        if sw:
            break
    if not sw:
        print('NO TIENE')
    