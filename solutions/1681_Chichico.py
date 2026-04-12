# https://jv.umsa.bo/oj/problem.php?id=1681
#  Chichico
#  Enviar
#  Estado
#  Descripción
#   Entrada
#   Salida
#   Ejemplo Entrada
#    3111223 5
#   Ejemplo Salida
#    323
#   Ayuda

#No funciona
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    i,j = min(a),max(a)
    print(i,j)