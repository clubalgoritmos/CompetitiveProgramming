N = int(input())
A = [int(x) for x in input().rstrip().split(" ")]
B = [int(x) for x in input().rstrip().split(" ")]
for i in range(N):
  S = input()
  if S=="+":
    A[i]+=B[i]
  elif S=="*":
    A[i]*=B[i]
  elif S==">":
    A[i] = A[i] if A[i]>B[i] else B[i]
  else:
    A[i] = A[i] if A[i]<B[i] else B[i]
del B
for i in A:
  print(i)