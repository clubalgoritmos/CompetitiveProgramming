for _ in range(int(input())):
  h,sh = (int(x) for x in input().split(' '))
  a,r=0,0
  if h-40 >0:
    a = h-40
    r = a*sh*1.5
  r = (h-a)*sh + r
  print("{:.2f}".format(r))