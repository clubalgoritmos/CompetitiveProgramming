n = int(input())
a = 0 
for i in range(n):
  V = list() 
  if n%2==0:
    if i<int(n/2): 
      a=a+1
    elif i>int(n/2): 
      a=a-1
  else:
    if i<int(n/2)+1: 
      a=a+1
    elif i>=int(n/2): 
      a=a-1
  for j in range(n):
    V.append(a)
  print(*V)


