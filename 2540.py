s = int(input())
M = list()
for i in range(s):
    M.append([0]*s)

while True:
  V = [int(x) for x in input().split(' ')]
  if V[0] == 1:
    M[V[1]][V[2]] = M[V[1]][V[2]]+V[3]
  elif V[0] == 2:
    s = 0
    for i in range(V[2], V[4]+1, 1):
      for j in range(V[1], V[3]+1, 1):
        s = s + M[i][j]
    print(s)
  elif V[0] == 3:
    break