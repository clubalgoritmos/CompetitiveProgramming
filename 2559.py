N, K = (int(x) for x in input().split(' '))
for _ in range(K):
  if N%10==0:
    N = N//10
  else:
    N = N-1
print(N)