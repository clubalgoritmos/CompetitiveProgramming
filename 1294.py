for _ in range(int(input())):
    N,i,j = map(int,input().split())
    A = list(map(int,input().split()))
    print(sum(A[i:j+1]))