import collections

N = int(input())
A = list(map(int, input().split()))
conjunto = set([i for i in range(1, N + 1)]) - set(A)
mx = A.index(max(A))
if A[mx]!=N:
    for i in range(1, N-A[mx]+1):
        A[mx-i]=A[mx]+i
for i, ai in enumerate(A):
    try:
        if ai == 0:  # rellenar
            if i < mx:  # creciente
                conjuntoA = conjunto.copy()
                Ab = min(conjuntoA)
                while Ab < A[i - 1] and A[i-1]!=0:
                    conjuntoA.remove(Ab)
                    Ab = min(conjuntoA)
                A[i] = Ab
                conjunto.remove(Ab)
            else:  # decreciente
                conjuntoA = conjunto.copy()
                Ab = max(conjuntoA)
                while Ab > A[i - 1] and A[i-1]!=0:
                    conjuntoA.remove(Ab)
                    #print(A,conjuntoA)
                    Ab = max(conjuntoA)
                A[i] = Ab
                conjunto.remove(Ab)
    except ValueError:
        print(A)
        break
else:
    print(*A)
    exit()
print("*")