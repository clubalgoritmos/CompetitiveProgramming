R, C = map(int,input().split(" "))
M = [[int(x) for x in input().split(" ")]for _ in range(R)]

def buscarM(x):
  for i in range(R):
    try:
      if (j:= M[i].index(x))!=None:
        return i, j
    except:
      pass
  return 0,0

def obtvecinos(i,j):
  if (0<=i-1 and i-1<R):
    vecinos.add(M[i-1][j])
  if (0<=i+1 and i+1<R):
    vecinos.add(M[i+1][j])
  if (0<=j-1 and j-1<C):
    vecinos.add(M[i][j-1])
  if (0<=j+1 and j+1<C):
    vecinos.add(M[i][j+1])

def buscarmenorvecino(x):
  try:
    while True:
      p = min(vecinos)
      if p>x:
        return p
      else:
        vecinos.remove(p)
  except:
    return False

maxc=0
for q in range(1, R*C+1):
  vecinos=set()
  o=q
  c=0
  p=None
  while True:
    c+=1
    i,j = buscarM(o)
    obtvecinos(i,j)
    p = buscarmenorvecino(o)
    if not p:
      break
    o=p
  if c>maxc:
    maxc=c
print(maxc)