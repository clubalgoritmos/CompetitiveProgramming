# https://jv.umsa.bo/oj/problem.php?cid=2862&pid=1
## https://jv.umsa.bo/oj/problem.php?id=1653
#  PRIMOS AMIGOS
#  Estado
#  Descripción
#    Hace pocos dias se ha realizado el Congreso Mundial de Matematicas y se ha decidio llamar números primos amigos a los que tienen MAXIMO COMÚN DIVISOR IGUAL a 1, anteriormente estos se llamaban primos relativos pero se a decidido cambiarles el nombre, tu tarea es ver si dos numeros son PRIMOS AMIGOS
#   Entrada
#    Se te daran pares de números hasta fin de archivo, los números no seran mayores a 1000.
#   Salida
#    Debes imprimir PRIMOS AMIGOS si es que se cumple que son PRIMOS AMIGOS ambos números y PRIMOS ENEMIGOS en caso CONTRARIO.
#   Ejemplo Entrada
#    7 49 2020 45 25
#   Ejemplo Salida
#    PRIMOS AMIGOSPRIMOS AMIGOSPRIMOS ENEMIGOSPRIMOS ENEMIGOS
#   Ayuda

import math
while True:
    try:
        a, b = map(int,input().split())
        if math.gcd(a,b)==1:
            print("PRIMOS AMIGOS")
            continue
        print("PRIMOS ENEMIGOS")
    except EOFError:
        break