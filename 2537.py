n =  int(input())
s = 0
M = [[int(x) for x in input().split(' ')] for _ in range(n)]
for i in range(n):
    if M[i][0] + M[i][1] + M[i][2] > 1:
      s = s+1
print(s)