# https://jv.umsa.bo/oj/problem.php?id=1435
#  El k-esimo dígito
#  Enviar
#  Estado
#  Descripción
#    Dado un número entero $N$ averiguar la cantidad de dígitos que tiene esté número, y además determinar cual es su $k$-esimo dígito.
#    Dado un número entero $N$ averiguar la cantidad de dígitos que tiene esté número, y además determinar cual es su $k$-esimo dígito.
#    Dado un número entero $N$ averiguar la cantidad de dígitos que tiene esté número, y además determinar cual es su $k$-esimo dígito.
#    Por ejemplo para $N =18421$ y $k = 3$, el número tiene $5$ dígitos y el tercer dígito es $4$.
#    Por ejemplo para $N =18421$ y $k = 3$, el número tiene $5$ dígitos y el tercer dígito es $4$.
#    Por ejemplo para $N =18421$ y $k = 3$, el número tiene $5$ dígitos y el tercer dígito es $4$.
#   Entrada
#    La entrada consta de dos números $N$ ($1 \leq N \leq 10^{18}$), el número a evaluar, y $K$ el dígito que estamos interesados en conocer, se garantiza que $K$ siempre será menor o igual al número de dígitos de $N$.
#    La entrada consta de dos números $N$ ($1 \leq N \leq 10^{18}$), el número a evaluar, y $K$ el dígito que estamos interesados en conocer, se garantiza que $K$ siempre será menor o igual al número de dígitos de $N$.
#    La entrada consta de dos números $N$ ($1 \leq N \leq 10^{18}$), el número a evaluar, y $K$ el dígito que estamos interesados en conocer, se garantiza que $K$ siempre será menor o igual al número de dígitos de $N$.
#   Salida
#    La salida consta de dos números separados por un espacio, la cantidad de dígitos del número $N$, y el $k$-ésimo dígito de este
#    La salida consta de dos números separados por un espacio, la cantidad de dígitos del número $N$, y el $k$-ésimo dígito de este
#    La salida consta de dos números separados por un espacio, la cantidad de dígitos del número $N$, y el $k$-ésimo dígito de este
#   Ejemplo Entrada
#    18421 3
#   Ejemplo Salida
#    5 4
#   Ayuda
#    Ejemplo de Entrada 2:196715 2Ejemplo de Salida 2:6 9
#    Ejemplo de Entrada 2:
#    Ejemplo de Entrada 2:
#    Ejemplo de Entrada 2:
#    196715 2Ejemplo de Salida 2:6 9
#    196715 2Ejemplo de Salida 2:6 9
#    Ejemplo de Salida 2:

import math
N,k = map(int,input().split())
print(int(math.log10(N))+1, (N//10**(k-1))%10)