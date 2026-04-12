# https://jv.umsa.bo/oj/problem.php?cid=2825&pid=3
## https://jv.umsa.bo/oj/problem.php?id=1739
#  Serie 3
#  Enviar
#  Estado
#  Descripción
#    Genere la serie 35 8 43 7 50 5 55 10 65 11...
#    Genere la serie
#    35 8 43 7 50 5 55 10 65 11...
#    Fíjese que tiene que ver la suma de los dígitos de un número en este problema.
#   Entrada
#    La primera línea son lo casos de prueba.
#    Por cada caso de prueba se lee un número n entero mayor a 0
#   Salida
#    Una sola fila por cada caso de prueba, separado de espacios
#   Ejemplo Entrada
#    236
#   Ejemplo Salida
#    35  8  4335  8  43  7  50  5
#   Ayuda
for _ in range(int(input())):
    N = int(input())
    a = 35
    b = 0
    v = []
    for i in range(N):
        if i%2==0:
            a+=b
            v.append(a)
        else:
            b=sum(int(digit) for digit in str(a))
            v.append(b)
    print(*v,sep="  ")