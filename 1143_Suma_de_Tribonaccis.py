# https://jv.umsa.bo/oj/problem.php?id=1143
#  Suma de Tribonaccis
#  Enviar
#  Estado
#  Descripción
#    Como competidor ICPC es seguro que ya conoces la popular serie de Fibonacci, pero si no te han hablado de tribonacci este es el momento.
#    Los términos de esta singular serie son 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, asumiendo que los tres primeros terminos forman la base de la serie y calcular el cuarto termino requiere sumar 0+1+1=2 y el quinto termino 1+1+2=4.
#    Básicamente se pide hacer la suma de los n términos generados, por ejemplo si introducirnos 5 deberá sumar 0+1+1+2+4=8 o si introducimos 7 se calculara 0+1+1+2+4+7+13=28.
#   Entrada
#    La primera línea indica la cantidad de casos de prueba, seguidamente los casos de prueba, cada caso de prueba indica una cantidad C de términos de la serie a sumar donde 1<=c<=40.
#    La primera línea indica la cantidad de casos de prueba
#   Salida
#    La salida es un número que señala la suma de los c términos de la serie.
#    La salida es un número que señala la suma de los c términos de la serie.
#   Ejemplo Entrada
#    6123102040
#   Ejemplo Salida
#    0121777865215441923556
#   Ayuda
#    Simulamos el proceso descrito, acumulando las sumas que tenemos hasta cierto punto para luego
#    responder las querys.
tribo = [0, 1, 1]

def tribonacci(n):
    if n < len(tribo):
        return tribo[:n]
    tribo.append(tribo[-1]+tribo[-2]+tribo[-3])
    return tribonacci(n)

for _ in range(int(input())):
    n = int(input())
    tribonacci(n)
    print(sum(tribo[:n]))