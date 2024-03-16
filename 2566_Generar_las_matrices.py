# https://jv.umsa.bo/oj/problem.php?id=2566
#  Generar las matrices
#  Enviar
#  Estado
#  Descripción
#    Dado un n donde 2 <= n <= 100, se pide generar la siguiente matriz.
#    Dado un n donde 2 <= n <= 100, se pide generar la siguiente matriz.
#    Dado un n donde 2 <= n <= 100, se pide generar la siguiente matriz.
#   Entrada
#    Un simple número natural n donde 2 <= n <= 100
#    Un simple número natural n donde 2 <= n <= 100
#    Un simple número natural n donde 2 <= n <= 100
#   Salida
#    Cada número debe estar separado por un espacio(el último número de cada fila no tiene espacio) y cada fila está en un línea.
#    Cada número debe estar separado por un espacio(el último número de cada fila no tiene espacio) y cada fila está en un línea.
#    Cada número debe estar separado por un espacio(el último número de cada fila no tiene espacio) y cada fila está en un línea.
#   Ejemplo Entrada
#    5
#   Ejemplo Salida
#    1 1 1 1 12 2 2 2 23 3 3 3 32 2 2 2 21 1 1 1 1
#   Ayuda

n = int(input())
a = 0 
for i in range(n):
  V = list() 
  if n%2==0:
    if i<int(n/2): 
      a=a+1
    elif i>int(n/2): 
      a=a-1
  else:
    if i<int(n/2)+1: 
      a=a+1
    elif i>=int(n/2): 
      a=a-1
  for j in range(n):
    V.append(a)
  print(*V)


