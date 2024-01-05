N=int(input())
arr=list(map(int,input().split()))
Q,X = map(int,input().split())
c=0
for a in arr:
  if a>X:
    c+=1
if c<Q:
  print("POSTULA")
else:
  print("NO POSTULES")