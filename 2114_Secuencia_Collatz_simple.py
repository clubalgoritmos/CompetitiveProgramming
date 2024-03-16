# https://jv.umsa.bo/oj/problem.php?id=2114
#  Secuencia Collatz simple
#  Enviar
#  Estado
#  Descripción
#   Entrada
#   Salida
#   Ejemplo Entrada
#    211123456
#   Ejemplo Salida
#    623
#   Ayuda

for _ in range(int(input())):
    n = int(input())
    c=0
    while n>1:
        c+=1
        if n%2==0:
            n//=2
        else:
            n+=1
    print(c)
