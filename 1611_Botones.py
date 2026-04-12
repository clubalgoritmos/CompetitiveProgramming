# https://jv.umsa.bo/oj/problem.php?id=1611
#  Botones
#  Enviar
#  Estado
#  Descripción
#   Entrada
#   Salida
#   Ejemplo Entrada
#    5 31 4 2 3 3
#   Ejemplo Salida
#    SI
#   Ayuda
#    En el caso de prueba el botón 0 esta prendido, al apretarlo se encenderá el botón 1 y se apagara el botón 0, al apretar el botón 1 se encenderá el botón 4 y se apagara el botón 1 y al apretar el botón 4 se encenderá el botón 3 y se apagara el botón 4.
#    Ejemplo de Entrada 2
#    3 1
#    0 1 1
#    Ejemplo de Salida 2
#    NO
#    Como el botón 0 tiene escrito encima el mismo número entonces al apretarlo el botón permanecerá encendido y ninguno más se prendera.

N, M = map(int, input().split(" "))
K = 0
b = set()
a = list(map(int, input().rstrip().split(" ")))
while K not in b:
  b.add(K)
  K = a[K]
  if K==M:
    break
if K==M:
  print("SI")
else:
  print("NO")