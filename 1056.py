for _ in range(int(input())):
    n = input()
    A = list(map(int,input().split()))
    A.reverse()
    for a in A:
        print(a,end=" ")
    print()