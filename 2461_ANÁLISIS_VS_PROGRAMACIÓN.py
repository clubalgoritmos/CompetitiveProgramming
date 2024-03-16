# https://jv.umsa.bo/oj/problem.php?cid=2567&pid=6
#  ANÁLISIS VS PROGRAMACIÓN
#  Estado
#  Descripción
#    Dado un valor x y un valor de n, realizar un programa para calcula la siguiente fórmula:
#    Dado un valor x y un valor de n, realizar un programa para calcula la siguiente fórmula:
#   Entrada
#    En la primera línea esta en número de casos, y en cada línea siguiente los casos de referencia, separados por un espacio.
#    En la primera línea esta en número de casos, y en cada línea siguiente los casos de referencia, separados por un espacio.
#   Salida
#    Se imprime el resultado sin decimales, sólo la parte entera.
#    Se imprime el resultado sin decimales, sólo la parte entera.
#   Ejemplo Entrada
#    42 32 53 33 5
#   Ejemplo Salida
#    48927
#   Ayuda

#Programación
#for _ in range(int(input())):
#  x, n = (int(x) for x in input().split(' '))
#  s = 1
#  for i in range(1, n+1):
#    s = s * (x**(i/n))
#  print(round(s))

#Analisis
for _ in range(int(input())):
  x, n = (int(x) for x in input().split(' '))
  s = 1
  for i in range(1, n):
    s+=i/n
  print(round(x**(s)))