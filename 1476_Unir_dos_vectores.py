# https://jv.umsa.bo/oj/problem.php?id=1476
#  Unir dos vectores
#  Enviar
#  Estado
#  Descripción
#    Se te dará dos números $N$ y $M$ los tamaños de dos vectores $A$ y $B$ se te pide crear un tercer vector $C$ que contenga todos los elementos de $A$ y $B$, ordenados de menor a mayor
#    Se te dará dos números $N$ y $M$ los tamaños de dos vectores $A$ y $B$ se te pide crear un tercer vector $C$ que contenga todos los elementos de $A$ y $B$, ordenados de menor a mayor
#    Se te dará dos números $N$ y $M$ los tamaños de dos vectores $A$ y $B$ se te pide crear un tercer vector $C$ que contenga todos los elementos de $A$ y $B$, ordenados de menor a mayor
#   Entrada
#    La primera línea consta de dos números $N$, $M$ ($1 \leq N,M \leq 100$), la segunda línea contendrá los $N$ elementos del vector $A$ y la tercera línea los $M$ elementos del vector $B$.
#    La primera línea consta de dos números $N$, $M$ ($1 \leq N,M \leq 100$), la segunda línea contendrá los $N$ elementos del vector $A$ y la tercera línea los $M$ elementos del vector $B$.
#    La primera línea consta de dos números $N$, $M$ ($1 \leq N,M \leq 100$), la segunda línea contendrá los $N$ elementos del vector $A$ y la tercera línea los $M$ elementos del vector $B$.
#   Salida
#    Imprimir el nuevo vector $C$ ordenado de menor a mayor un elemento por línea.
#    Imprimir el nuevo vector $C$ ordenado de menor a mayor un elemento por línea.
#    Imprimir el nuevo vector $C$ ordenado de menor a mayor un elemento por línea.
#   Ejemplo Entrada
#    4 31 2 3 43 5 6
#   Ejemplo Salida
#    1233456
#   Ayuda

N, M = map(int, input().split())
A, B = list(map(int, input().split(" "))), list(map(int, input().split(" ")))
for i in sorted(A+B):
  print(i)