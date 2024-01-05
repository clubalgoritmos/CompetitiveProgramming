a,b = map(int, input().split())
def fun(n):
  n = int(n)
  if a<=n and n<=b:
    return True
  return False
print(sum([int(x) for x in input().split() if fun(x)]))