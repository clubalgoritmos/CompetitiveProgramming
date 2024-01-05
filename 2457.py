t = int(input())
for i in range(t):
 a,b,c = (int(x) for x in input().split())
 if a==b+c or b==a+c or c==a+b:
  print('SI')
 else:
  print('NO')