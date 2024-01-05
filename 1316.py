import sys
for i in sys.stdin:
  N = int(i)
  A = [int(x) for x in input().rstrip().split(" ")]
  B = [int(x) for x in input().rstrip().split(" ")]
  A.sort(reverse = True)
  B.sort()
  resultado = [a*b for a, b in zip(A, B)]
  print(sum(resultado))