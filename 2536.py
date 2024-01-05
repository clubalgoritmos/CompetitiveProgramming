t = int(input())
for i in range(t):
 a = input()
 if len(a)>10:
  V=[x for x in a]
  a=f"{V[0]}{len(V)-2}{V[-1]}"
 print(a)