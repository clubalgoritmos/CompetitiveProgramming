import sys
for i in sys.stdin:
  a,b = map(int, i.split(" "))
  resultado = ""
  for i in range(max(len(bin(a)[2:]), len(bin(b)[2:]))):
      if i < len(bin(a)[2:]):
          resultado += bin(a)[2:][i]
      if i < len(bin(b)[2:]):
          resultado += bin(b)[2:][i] 
  print(resultado)