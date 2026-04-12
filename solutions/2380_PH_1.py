# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=202
## https://jv.umsa.bo/oj/problem.php?id=2380
#    Copiado al portapapeles
#  PH 1
#  Enviar
#  Estado
#  Descripción
#    Los números primos son aquellos que son solo divisibles por si mismo o el uno.
#   Entrada
#    La entrada consiste den:
#    - La primera línea contiene el número de casos de prueba
#    - Las líneas siguientes corresponden a los casos de prueba, de dos enteros a,b
#    - Las
#    líneas
#    siguientes corresponden a los casos de prueba, de dos enteros a,b
#   Salida
#    Se debe mostrar por cada prueba, una línea con el número de primos existente entre intervalo a y b
#    Se debe mostrar por cada prueba, una línea con el número de primos existente entre intervalo a
#    a
#    y b
#    b
#   Ejemplo Entrada
#    42 1000100000 10000001000000 100000002 10000000
#   Ejemplo Salida
#    16868906586081664579
#   Ayuda

def criba_de_eratostenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve
sieve = criba_de_eratostenes(10**7)
for _ in range(int(input())):
    a, b = map(int,input().split())
    print(sum(sieve[a:b+1]))
    
    