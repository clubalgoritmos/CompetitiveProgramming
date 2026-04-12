# https://jv.umsa.bo/oj/problem.php?id=1504
#  Ordenando el Laboratorio
#  Enviar
#  Estado
#  Descripción
#    Max es un tipo muy ordenado,  pero tiene un problema, despues de haber supuestamente ordenado, no sabe si la forma en la que esta ordenado el laboratorio esta bien. Su laboratorio esta representado por una grilla cuadrada de n x n. El laborotario esta “Bien ordenado” si para cada numero distinto de 1 se puede expresar como la suma de un numero en la misma fila con un numero en la misma columna.  En otras palabras, para cada x,y (1 <= x,y <= n) and a_x,y != -1 debe existir dos indices s y t  talque  a_x,y =  a_x,s + a_t,y donde I  es la fila y j es la columna. Ayuda a Max a verificar si su laboratorio esta “Bien ordenado”.
#   Entrada
#    La primera linea contiene t, el numero de casos de prueba
#    La siguiente linea contiene un entero n (1 <= n <= 50) el tamanho del laboratorio.
#    Luego se representa el laboratorio de n x n.  1 <= a_i,j <= 100000 donde I es la fila y j es la columna en la grilla.
#   Salida
#    mprima “Si” si esta bien ordenado, de lo contrario “No”.
#   Ejemplo Entrada
#    131 1 22 3 16 4 1
#   Ejemplo Salida
#    Si
#   Ayuda

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