#Time limit
D,C,R=map(int, input().split())
Cv=[int(input()) for _ in range(C)]
for _ in range(R): D+=int(input())
con = 0
for Ci in Cv:
  D-=Ci
  if D>0:
    con+=1
print(con+R)