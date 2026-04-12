# https://jv.umsa.bo/oj/problem.php?cid=2575&pid=9
#  Sucesion imposible
#  Estado
#  Descripción
#    Generar n términos de la siguiente sucesión de números:
#    0
#    1 1
#    2
#    2
#    2
#    3
#    3
#    3
#    3
#    4
#    4
#    4
#    4
#    4
#    . . . . . . . . . .
#   Entrada
#   Salida
#   Ejemplo Entrada
#    20
#   Ejemplo Salida
#    0, 2, 1, 1, 3, 2, 2, 2, 5, 3, 3, 3, 3, 7, 4, 4, 4, 4, 4, 11
#   Ayuda

N = int(input())
count = 0
i = 0
lastprime = 1
result = []

def nextprime(n):
    while True:
        n += 1
        for i in range(2,n):
            if n % i == 0:
                break
        else:
            return n

while count < N:
    for _ in range(-1,i):
        if count < N:
            result.append(str(i))
            count += 1
        else:
            break
    else:
        if count >= N:
            continue
        lastprime = nextprime(lastprime)
        count+=1
        result.append(str(lastprime))
    i += 1

print(', '.join(result))