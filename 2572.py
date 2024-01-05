for _ in range(int(input())):
  V = [int(float(x)) for x in input().strip('\r')]
  s = 0
  a = 0
  for i in range(len(V)-1):
    if V[i] == 1 and V[i+1] == 0:
      V[i], V[i+1] = 10, 0
  for x in V:
    s=s+x
    if x!=0:
      a=a+1
  print("{:.2f}".format(s/a))