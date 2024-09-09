#Solucion
N,H,W = map(int, input().split(" "))
for _ in range(N):
  a,b = (x.lower() for x in input().split())
  i,j = "N", "N"
  if (a=="y" or W<=0):
    i="Y"
    W+=1
    H-=1
  if (b=="y" or H<=0):
    j="Y"
    H+=1
    W-=1
  print(i,j)