code = "MURCIELAGO"
for _ in range(int(input())):
  r = ""
  for c in input().upper():
    if c in code:
      r = r + str(code.find(c))
    else:
      r = r + c
  print(r)