def Buscar(y,x,a):
  if a==1:
    return True
  fila={M[y][i] for i in range(N) if M[y][i]<=a and x!=i}
  columna={M[j][x] for j in range(N) if M[j][x]<=a and y!=j}
  for filaele in fila:
    for columnaele in columna:
      if filaele+columnaele==a:
        return True
  return False

def BuscarM():
  for y in range(N):
      for x in range(N):
        if not Buscar(y,x,M[y][x]):
          return "No"
      return "Si"

for _ in range(int(input())):
  N = int(input())
  M = [[int(x) for x in input().split(" ")] for _ in range(N)]
  print(BuscarM())