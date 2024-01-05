n, k = (int(x) for x in input().split(' '))
v = [int(x) for x in input().split(' ')]
aux = v[0]
for i in range(k-1, n, k):
  v[i], aux = aux, v[i]
v[0] = aux
print(*v)