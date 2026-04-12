# https://jv.umsa.bo/oj/problem.php?cid=2826&pid=28
## https://jv.umsa.bo/oj/problem.php?id=2347
#  No Way Home
#  Enviar
#  Estado
#  Descripción
#    ¡Se acaba de estrenar la nueva película "Spider-Man: No Way Home"! Hay $n$ personas en la taquilla del cine paradas en una fila enorme. Cada uno de ellos tiene un solo billete de $100$, $50$ o $25$ bolivianos(solo existen estos tres tipos de biletes).
#    Un boleto para "Spider-Man: No Way Home" cuesta $25$ bolivianos. ¿Puede el empleado de reservas vender un boleto a cada persona y dar el cambio si inicialmente no tiene dinero y vende los boletos estrictamente en el orden que siguen las personas en la fila?
#   Entrada
#    La primera linea contiene el numero de casos de prueba.
#    La primera línea de cada caso de prueba contiene el número entero $n$ ($1\leqn\leq10^5$) — el número de personas en la fila del cine. La siguiente línea contiene $n$ enteros, cada uno de ellos es igual a $25$, $50$ o $100$, los valores de los billetes que tiene la gente. Los números se dan en el orden desde el principio de la fila (en la taquilla) hasta el final de la fila.
#   Salida
#    Imprima "SÍ" (sin las comillas) si el encargado de la reserva puede vender un boleto a cada persona y dar el cambio. De lo contrario, imprima "NO".
#   Ejemplo Entrada
#    1425 25 50 50
#   Ejemplo Salida
#    SI
#   Ayuda
#    Ejemplo de entrada 2:450 50 25 25
#    Ejemplo de entrada 2:
#    450 50 25 25
#    Ejemplo de salida 2:NO
#    Ejemplo de salida 2:
#    NO

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    c = 0
    for a in A:
        if a-25 > c:
            print("NO")
            break
        c += 25
        c -= a-25
    else:
        print("SI")