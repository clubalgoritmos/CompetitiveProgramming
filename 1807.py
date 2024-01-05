import sys
for i in sys.stdin:
  n = int(i)
  if (n%4==0 or n%7==0) or (set(map(int, str(n)))=={4,7}):
    print("YES")
  else:
    print("NO")