t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    for i in range(1,6):
        if (s%5)%i != 0:
            print(i)
            break
