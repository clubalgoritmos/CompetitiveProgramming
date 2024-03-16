F,C=map(int,input().split())
S = 0
M = [list(input()) for _ in range(F)]

for i in range(F):
    for j in range(C):
        if M[i][j]=="*":
            if i-1>=0 and M[i-1][j]!="*":
                S+=1
            if i+1<F and M[i+1][j]!="*":
                S+=1
            if j-1>=0 and M[i][j-1]!="*":
                S+=1
            if j+1<C and M[i][j+1]!="*":
                S+=1
            if i-1>=0 and j-1>=0 and M[i-1][j-1]!="*":
                S+=1
            if i-1>=0 and j+1<C and M[i-1][j+1]!="*":
                S+=1
            if i+1<F and j-1>=0 and M[i+1][j-1]!="*":
                S+=1
            if i+1<F and j+1<C and M[i+1][j+1]!="*":
                S+=1
            S+=9
print(S)