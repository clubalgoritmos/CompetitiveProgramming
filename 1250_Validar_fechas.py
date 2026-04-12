# https://jv.umsa.bo/oj/problem.php?id=1250
#  Validar fechas
#  Enviar
#  Estado
#  Descripción
#   Entrada
#   Salida
#    En la salida imprima "Fecha correcta" si la fecha es correcta, o por el contrario "Fecha incorrecta"
#   Ejemplo Entrada
#    230 11 197129 2 2001
#   Ejemplo Salida
#    Fecha correctaFecha incorrecta
#   Ayuda

mv = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for _ in range(int(input())):
  d, m, y = map(int,input().split(" "))
  try:
    if d>=0 and (d<=mv[m] or (d<=29 and m==2 and (y/4)%100==0)):
      print("Fecha correcta")
    else:
      raise 
  except:
    print("Fecha incorrecta")
