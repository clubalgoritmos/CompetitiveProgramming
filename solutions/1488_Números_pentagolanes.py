# https://jv.umsa.bo/oj/problem.php?cid=2823&pid=12
## https://jv.umsa.bo/oj/problem.php?id=1488
#  Números pentagolanes
#  Enviar
#  Estado
#  Descripción
#    Talvisota es un niño muy curioso, su curiosidad comenzó al saber por que alguien le pondría Talvisota, pero bueno en su clase de matemáticas de hoy vio los números triangulares, seguro ya los conoces, la idea es la siguiente si tuvieras muchas fichas con cuantas puedes formar triángulos. Vieron que esto se cumplía para 1, 3, 6, 10, 15 y así sucesivamente.
#    Llegado este punto supongo que te diste cuenta cómo se generan, son la suma de los primeros n números naturales.
#    Pues bien basados en esta idea Talvisota se dijo con cuantas fichas puedo formar pentagonos dentro de pentágonos y esto es lo que obtuvo.
#    Ahora Talvisota te pide tu ayuda para poder ver esta serie con mayor detenimiento.
#   Entrada
#    La entrada consiste de un número $n$ ($0 \leq n \leq 10^{3}$), para el cual se deberá mostrar toda la serie descrita anteriormente hasta el elemento $n$ de la serie.La entrada termina cuando no hay mas elementos por leer.
#   Salida
#    La salida será $n$ números separados por un espacio, que son los números que forman la serie
#   Ejemplo Entrada
#    5
#   Ejemplo Salida
#    1 5 12 22 35 
#   Ayuda

pentagonal_number = lambda n: (3*n*n - n) // 2
memo = []

while True:
    try:
        N = int(input())
        if N > len(memo)-1:
            for i in range(len(memo), N):
                memo.append(pentagonal_number(i+1))
        print(" ".join(map(str, memo)))
    except EOFError:
        break