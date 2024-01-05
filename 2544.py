x,y,z = 0,0,0
for _ in range(int(input())):
  a,b,c = (int(i) for i in input().split(' '))
  x,y,z = x+a,y+b,z+c
if x+y+z == 0:
  print('SI')
else:
  print('NO')