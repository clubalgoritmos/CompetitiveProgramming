N, M = map(int, input().split(" "))
K = 0
b = set()
a = list(map(int, input().rstrip().split(" ")))
while K not in b:
  b.add(K)
  K = a[K]
  if K==M:
    break
if K==M:
  print("SI")
else:
  print("NO")