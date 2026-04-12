# https://jv.umsa.bo/oj/problem.php?id=1009
#  Mi música Favorita
#  Enviar
#  Estado
#  Descripción
#    Tendrás que hacer un viaje muy largo a otra ciudad, así que una muy buena compañía será tu música favorita. Tu auto cuenta con una lector de casetes, pero existe un pequeño inconveniente ya que tu música favorita se encuentra en CD's. Así que es necesario grabar tu música del CD al casete en los
#    Tendrás que hacer un viaje muy largo a otra ciudad, así que una muy buena compañía será tu música favorita. Tu auto cuenta con una lector de casetes, pero existe un pequeño inconveniente ya que tu música favorita se encuentra en CD's. Así que es necesario grabar tu música del CD al casete en los
#    N minutos disponibles en el casete (Ya que existe el límite de la cinta de casete).
#    N minutos disponibles en el casete (Ya que existe el límite de la cinta de casete).
#    El objetivo del problema es llenar el máximo número de minutos posibles en la cinta del casete.
#    El objetivo del problema es llenar el máximo número de minutos posibles en la cinta del casete.
#   Entrada
#    La primera línea de entrada consiste en el número de casos de prueba TC 1<=TC<=10.
#    La primera línea de entrada consiste en el número de casos de prueba TC
#    La primera línea de entrada consiste en el número de casos de prueba TC
#    1<=TC<=10
#    1<=TC<=10
#    Por cada caso de prueba habra un entero N 1<=N<=1500 (minutos que soporta la cinta del casete), seguidamente por un entero T 1<=T<=20 (número de pistas que tiene el CD) seguidamente por Ti<=N (1<=i<=N) eneros que representa el tiempo de duración de cada pista.
#    Por cada caso de prueba habra un entero N
#    Por cada caso de prueba habra un entero N
#    1<=N<=1500
#    1<=N<=1500
#    (minutos que soporta la cinta del casete), seguidamente por un entero T
#    (minutos que soporta la cinta del casete), seguidamente por un entero T
#    1<=T<=20
#    1<=T<=20
#    =
#    =20
#    (número de pistas que tiene el CD) seguidamente por Ti<=N (1<=i<=N)
#    (número de pistas que tiene el CD) seguidamente por Ti<=N (1<=i<=N)
#    eneros que representa el tiempo de duración de cada pista
#    eneros que representa el tiempo de duración de cada pista
#   Salida
#    Imprimir por cada caso de prueba las pistas (la duración de cada pista)  que maximizan el uso de la cinta del casete.Si existen varios subconjuntos que maximizan la duracion, elija la configuracion la cual si marcaramos con 1 los cassetes que se eligen y con 0 los que no se eligen y tomaramos esos numeros como la representaciòn binaria de un numero decimal, elegir el que tenga mayor numero en decimal.
#    Imprimir por cada caso de prueba las pistas (la duración de cada pista)  que maximizan el uso de la cinta del casete.Si existen varios subconjuntos que maximizan la duracion, elija la configuracion la cual si marcaramos con 1 los cassetes que se eligen y con 0 los que no se eligen y tomaramos esos numeros como la representaciòn binaria de un numero decimal, elegir el que tenga mayor numero en decimal.
#    Imprimir por cada caso de prueba las pistas (la duración de cada pista)  que maximizan el uso de la cinta del casete.Si existen varios subconjuntos que maximizan la duracion, elija la configuracion la cual si marcaramos con 1 los cassetes que se eligen y con 0 los que no se eligen y tomaramos esos numeros como la representaciòn binaria de un numero decimal, elegir el que tenga mayor numero en decimal.
#   Ejemplo Entrada
#    35 3 1 3 410 4 9 8 4 220 4 10 5 7 4
#   Ejemplo Salida
#    1 48 210 5 4
#   Ayuda
#    2da div. 2012 UMSA

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    n, t = arr[0], arr[1]
    arr = arr[2:]
    max_sum = 0
    best_subset = []
    for i in range(1, 1 << t):
        subset = [arr[j] for j in range(t) if i & (1 << j)]
        subset_sum = sum(subset)
        if subset_sum <= n and subset_sum > max_sum:
            max_sum = subset_sum
            best_subset = subset
    print(*best_subset)