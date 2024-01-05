n = int(input())
P = [x for x in input().upper()]
s = 0
for i in range(1, n):
  if P[i-1] == P[i]:
    s+=1
print(s)