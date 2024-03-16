import sys
for i in sys.stdin:
  N = int(i)
  n = int(N**(1/3))
  a = (N//n)
  if a%2==0:
    a = a-1
  else:
    a = a
  print(a)