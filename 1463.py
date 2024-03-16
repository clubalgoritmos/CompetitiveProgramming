#no funcioan

N = int(input())
A = [0]*N
A[0]=N
def correcto():
    for i in range(N):
        if A[i] != A.count(i):
            return False
    return True

if N == 1:
    print("-1")
else:
    while not correcto():
        last = A.copy()
        for i in range(N):
            A[i] = A.count(i)
        if last == A:
            print("-1")
            break
    else:
        for a in A:
            print(a, end="\n")