# https://jv.umsa.bo/oj/problem.php?cid=2822&pid=1
## https://jv.umsa.bo/oj/problem.php?id=1890
#  Formando Amigos
#  Enviar
#  Estado
#  Descripción
#    En los concursos de progamacion n de losparticipantes de la competencia se dividieron enmequipos de alguna manera para que cada equipo tenga al menos un participante.Después de la competencia, cada par de participantes del mismo equipo se hizo amigo.
#    En los concursos de progamacion n de los
#    m
#    Su tarea es escribir un programa que encuentre el número mínimo y máximo de pares de amigos que podrían haberse formado al final de la competencia.
#   Entrada
#    La primera linea contiene un entero t (0< t <100)que representa los casos de prueba, por cada caso de prueba habra una línea de entrada contiene dos enterosnym, separados por un solo espacio (1 ≤m≤n≤ 109): el número de participantes y el número de equipos respectivamente.
#    n
#    1 ≤m≤n≤ 109
#    9
#   Salida
#    Por cada caso de prueba imprima una línea de la salida debe contener dos enteroskminykmax: el número mínimo posible de pares de amigos y el número máximo posible de pares de amigos, respectivamente.
#    kmin
#    min
#    kmax
#    max
#   Ejemplo Entrada
#    35 13 26 3
#   Ejemplo Salida
#    10 101 13 6
#   Ayuda
#    En la primera muestra, todos los participantes se unen en un equipo, por lo que habrá exactamente diez pares de amigos.
#    En la segunda muestra, en cualquier arreglo posible, un equipo siempre tendrá dos participantes y el otro equipo siempre tendrá un participante.Por lo tanto, el número de pares de amigos siempre será igual a uno.
#    En la tercera muestra, se puede lograr un número mínimo de amistades recién formadas si los participantes se dividieron en equipos de2personas, el número máximo se puede lograr si los participantes se dividieron en equipos de1,1y4personas.
#    2
#    1
#    4
import math

t = int(input())
for _ in range(t):
    m,n = map(int,input().split())
    print(math.comb(m%n,2))