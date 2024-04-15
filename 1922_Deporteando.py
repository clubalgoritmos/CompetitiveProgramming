# https://jv.umsa.bo/oj/problem.php?id=1922
#  Deporteando
#  Enviar
#  Estado
#  Descripción
#    En un mundo extraño mientras Osvaldo caminaba por la calle, vio una tienda deportiva, como a Osvaldo le gusta jugar Futsal, Basquet y Wally, quiere comprar una pelota de cada tipo, pero luego se dio cuenta que existen pelotas en la tienda que pueden servir para jugar $1$ tipo de deporte o alguna combinación de los $3$ tipos, por ejemplo habia una pelota que servia para jugar Futsal y Wally, otra pelota que servia para jugar Futsal, Wally y Basquet, etc.
#    Esta información le resulto demasiado útil, ahora Osvaldo no necesariamente tendrá que comprar $3$ pelotas, Él quiere jugar los tres deportes, Cúal es el precio mínimo que tiene que pagar por las pelotas que comprará con tal de jugar los $3$ tipos de deportes?
#   Entrada
#    La primera linea contiene un número entero $N$, $(1 \leq N \leq 10 ^ 3)$, el número de pelotas en la tienda.
#    Cada una de la $N$ lineas contiene un número entero $C$, $(1 \leq C \leq 10 ^ 5)$ el precio de la pelota, y una cadena $S$ de tamaño de $1$ a $3$, esta cadena solo contiene las letras $'F'$, $'W'$, $'B'$, indicando que la pelota es para Futsal, Wally y Basquet respectivamente, esta garantizado que una letra a los más aparece una vez en la cadena, el orden de los caracteres es arbitrario.
#   Salida
#    Imprima $-1$ si no hay alguna posibilidad de obtener alguna combinación de los $3$ tipos de deportes, caso contrario imprima el costo mínimo que se necesita para comprar las pelotas y poder jugar los $3$ tipos de deportes.
#   Ejemplo Entrada
#    610 B9 FW11 WB4 B5 F20 W
#   Ejemplo Salida
#    13
#   Ayuda
#    En el ejemplo anterior la respuesta es $13$ porque si compramos la pelota con precio $[9, 4]$ con las dos pelotas podemos jugar los $3$ tipos de deportes, hay otras combinaciones como $[9, 11], [10, 9] , [11, 5], [4, 5, 20,] , [10, 5, 20]$, con estas combinaciones igual se puede jugar los $3$ tipos de deportes pero el costo es mayor que $13$.
#    Nota la combinación $4$ y $5$ no es valida porque solo podemos jugar $2$ tipos de deportes.

N = int(input())
balls = [tuple(input().split()) for _ in range(N)]
dp = [1e9]*8
dp[0] = 0
for c, s in balls:
    c = int(c)
    mask = 0
    if 'B' in s:
        mask |= 1
    if 'W' in s:
        mask |= 2
    if 'F' in s:
        mask |= 4
    for i in range(8):
        dp[i | mask] = min(dp[i | mask], dp[i] + c)
if dp[7] == 1e9:
    print(-1)
else:
    print(dp[7])