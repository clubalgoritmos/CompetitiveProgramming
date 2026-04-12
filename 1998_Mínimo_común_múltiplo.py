# https://jv.umsa.bo/oj/problem.php?cid=2824&pid=1
## https://jv.umsa.bo/oj/problem.php?id=1998
#  Mínimo común múltiplo
#  Estado
#  Descripción
#    El mínimo común múltiplo de dos números $a$ y $b$ es el número más pequeño que es múltiplo de $a$ y múltiplo de $b$.Para denotar el mínimo común múltiplo de $a$ y $b$ escribiremos $m.c.m.(a, b)$ ó $mcm(a, b)$.
#    Ejemplo:
#    Vamos a calcular el mínimo común múltiplo de $4$ y $6$. Para ello, escribimos los primeros múltiplos de $4$ y de $6$:
#    Entre los $6$ primeros múltiplos de $4$ y de $6$, los números $12$ y $24$ son múltiplos de ambos (son múltiplos comunes).
#    Tenemos que quedarnos con el mínimo.
#    Por tanto, el mínimo común múltiplo de $4$ y $6$ es $12$:
#   Entrada
#    La entrada contiene $t$ casos de prueba ($1 \leq t \leq 100$).Por cada caso de prueba se le dan dos números $a$ y $b$ ($1 \leq a \leq b \leq 1000$).
#   Salida
#    Por cada caso de prueba imprima el $mcm(a, b)$.
#   Ejemplo Entrada
#    55 74 63 97 162 9
#   Ejemplo Salida
#    3512911218
#   Ayuda
import math
 
for _ in range(int(input())):
    a,b = map(int,input().split())
    print((a*b)//math.gcd(a,b))