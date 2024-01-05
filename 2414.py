for _ in range(int(input())):
  n = int(input())
  i, x = 1, 1
  while x<n:
    i+=1
    x+=i
  if x==n:
    print(f"Llegas al cuadrado {i}")
  else:
    print("No llegas")