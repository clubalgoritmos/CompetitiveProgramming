# https://jv.umsa.bo/oj/problem.php?id=1450
#  Vectores2
#  Enviar
#  Estado
#  Descripción
#    Se tiene una lista de números y te piden hallar la suma entre dos valores $a$ y $b$. Se sabe que la suma no excede un numero entero.Sugerencia en java:
#    Se tiene una lista de números y te piden hallar la suma entre dos valores $a$ y $b$. Se sabe que la suma no excede un numero entero.Sugerencia en java:
#    Se tiene una lista de números y te piden hallar la suma entre dos valores $a$ y $b$. Se sabe que la suma no excede un numero entero.Sugerencia en java:
#    Leer los números como una linea.
#    Leer los números como una linea.
#    Convertir esta linea a una arreglo de cadenas con:
#    Convertir esta linea a una arreglo de cadenas con:
#    String [] vector = leer.nextLine().split(" ");
#    String [] vector = leer.nextLine().split(" ");
#    Cada elemento de vector convertir a numero con    Integer.parseInt(vector(i)). Tomar en cuenta que nextLine lee hasta el fin de linea.
#    Cada elemento de vector convertir a numero con    Integer.parseInt(vector(i)). Tomar en cuenta que nextLine lee hasta el fin de linea.
#    Sugerencia en Python:
#    Sugerencia en Python:
#    Sugerencia en Python:
#    Leer la lista en una sola linea: v = [int(x) for x in input().split()]
#    Leer la lista en una sola linea: v = [int(x) for x in input().split()]
#   Entrada
#    Cada caso de prueba consiste de dos líneas, la primera linea tiene son los números $a$ y $b$ separados por un espacio.La segunda línea contiene números separados por un espacio.
#    Cada caso de prueba consiste de dos líneas, la primera linea tiene son los números $a$ y $b$ separados por un espacio.La segunda línea contiene números separados por un espacio.
#    Cada caso de prueba consiste de dos líneas, la primera linea tiene son los números $a$ y $b$ separados por un espacio.La segunda línea contiene números separados por un espacio.
#   Salida
#    Por cada caso de prueba escrita en una linea la suma de los números cuyo valor están entre $a$ y $b$ inclusive.
#    Por cada caso de prueba escrita en una linea la suma de los números cuyo valor están entre $a$ y $b$ inclusive.
#    Por cada caso de prueba escrita en una linea la suma de los números cuyo valor están entre $a$ y $b$ inclusive.
#   Ejemplo Entrada
#    10 2010 2 10 1 20 31 5
#   Ejemplo Salida
#    40
#   Ayuda

a,b = map(int, input().split())
def fun(n):
  n = int(n)
  if a<=n and n<=b:
    return True
  return False
print(sum([int(x) for x in input().split() if fun(x)]))