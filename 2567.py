V = [x for x in input()]
aux = V[0]
B = aux
c = 0
for i in range(1, len(V)):
  if V[i] == aux:
    c = c+1
  else:
    aux = V[i]
    B = f"{B}{c}{aux}"
    c = 0
B = f"{B}{c}"
print(B)