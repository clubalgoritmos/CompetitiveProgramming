# https://jv.umsa.bo/oj/problem.php?id=2542
#  El lenguaje de programación INTI
#  Enviar
#  Estado
#  Descripción
#   Entrada
#   Salida
#   Ejemplo Entrada
#    3++xx++--x
#   Ejemplo Salida
#    1
#   Ayuda

x = 0
for _ in range(int(input())):
  a = input()
  if "+" in a:
    x+=1
  elif "-" in a:
    x-=1
print(x)