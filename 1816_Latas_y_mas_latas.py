# https://jv.umsa.bo/oj/problem.php?id=1816
#  Latas y mas latas
#  Enviar
#  Estado
#  Descripción
#    Una tarde estando Bob, en el Cuartel Patito notó que encima de un mueble habían algunas latas, el decidió ordenarlas (fig. 1) de modo que la base tenga $m$ latas, siguiendo de estas ($m-1$) latas, ($m-2$) latas, …, $2$ latas y por ultimo $1$ lata), después de haber ordenado sus latas, se preguntó cuántas latas quedarían si retirara una lata $j$ (índex 1)de la base y vio que al retirar una se caerían las dos latas de encima, cada una a su vez dejaría caer a dos más, y así sucesivamente (fig. 2).
#    Ahora Bob necesita tu ayuda, él desea saber cuántas latas quedarán en pie, Bob te dará el número de latas que componen la base y la posición de la lata que desea retirar (fig. 2).
#   Entrada
#    Se te dará un caso de prueba, que consistirá en dos enteros $m$ y $j$ descritos anteriormente ($1 \leq j \leq m \leq 1000000000$).
#   Salida
#    El número de latas que quedan en pie.
#   Ejemplo Entrada
#    43
#   Ejemplo Salida
#    4
#   Ayuda
#    Ejemplo de entrada 2:64
#    Ejemplo de salida 2: 9

m, j = int(input()), int(input())
levels = m - j
total_cans = (levels/2) * (2 + (levels-1)*2)
print(int(total_cans))asd