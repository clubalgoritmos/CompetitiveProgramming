for _ in range(int(input())):
  x, n = (int(x) for x in input().split(' '))
  s = 1
  for i in range(1, n+1):
    s = s * (x**(i/n))
  print(round(s))