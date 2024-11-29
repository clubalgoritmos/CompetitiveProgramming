from collections import Counter

h,w = map(int,input().split())
C = [list(input())*3 for _ in range(h)]*3
def t():
    for i in range(h*3):
        for j in range(w*3):
            for k in range(w*3-i):
                if len({C[i+k][j+k],C[i][j],C[i+k][j],C[i][j+k]})==4:
                    return True
    return False

if t():
    print("YES")
else:
    print("NO")
