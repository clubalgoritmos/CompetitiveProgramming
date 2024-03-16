for _ in range(int(input())):
    n = input()
    A = list(map(int,input().split()))
    c = 0
    while True:
        last = A.copy()
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                A[i],A[i+1] = A[i+1],A[i]
                c += 1
        if last==A:
            break
    print(c)