N = int(input())
M = [list(map(int,input().split())) for _ in range(N)]
mins = float('-inf')
x,y = 0,0
for i in range(N):
    mn = min(M[i])
    if mn > mins:
        mins = mn
        x = i
        y = M[i].index(mn)
if x==0 and y==0:
    print("3")
elif x==0 and y==N-1:
    print("2")
elif x==N-1 and y==0:
    print("0")
elif x==N-1 and y==N-1:
    print("1")

