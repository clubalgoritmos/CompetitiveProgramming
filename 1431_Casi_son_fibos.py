# https://jv.umsa.bo/oj/problem.php?id=1431
#  Casi son fibos
#  Enviar
#  Estado
#  Descripción
#    Todo el mundo conoce la serie de Fibonacci: $1,1,2,3,5,8,13,21,...$ En este caso estamos interesados en series parecidas módulo M, pero que inician en términos distintos al Fibonacci original por ejemplo $2,6,8,14,22,36,...$ o $9,11,20,31,51,...$ Debes imprimir el n-ésimo término módulo M de una de estás series.
#    Todo el mundo conoce la serie de Fibonacci: $1,1,2,3,5,8,13,21,...$ En este caso estamos interesados en series parecidas módulo M, pero que inician en términos distintos al Fibonacci original por ejemplo $2,6,8,14,22,36,...$ o $9,11,20,31,51,...$ Debes imprimir el n-ésimo término módulo M de una de estás series.
#    Todo el mundo conoce la serie de Fibonacci: $1,1,2,3,5,8,13,21,...$ En este caso estamos interesados en series parecidas módulo M, pero que inician en términos distintos al Fibonacci original por ejemplo $2,6,8,14,22,36,...$ o $9,11,20,31,51,...$ Debes imprimir el n-ésimo término módulo M de una de estás series.
#   Entrada
#    Se te dará un número N (1 <= N <= 10000) el n-ésimo término que debes imprimir, M (a,b < M <= 1000)el módulo y dos números a, b (1 <= a,b <= 1000)los términos inciales de la serie.
#    Se te dará un número N (1 <= N <= 10000) el n-ésimo término que debes imprimir, M (a,b < M <= 1000)el módulo y dos números a, b (1 <= a,b <= 1000)los términos inciales de la serie.
#    Se te dará un número N (1 <= N <= 10000) el n-ésimo término que debes imprimir, M (a,b < M <= 1000)el módulo y dos números a, b (1 <= a,b <= 1000)los términos inciales de la serie.
#   Salida
#    Imprimir el n-simo término de la serie módulo M.
#    Imprimir el n-simo término de la serie módulo M.
#    Imprimir el n-simo término de la serie módulo M.
#   Ejemplo Entrada
#    4 10 1 7
#   Ejemplo Salida
#    5
#   Ayuda

#CASI FIBOS

line = input().split()
modulo = int(line[1])
pre, pos = int(line[2]), int(line[3])
n = int(line[0])
val = 0
if n == 1:
    print(pre)
if n == 2:
    print(pos)
if n > 2:
    for i in range(3, n+1):
        val = pre + pos
        pre = pos
        pos = val

    print(val%modulo)