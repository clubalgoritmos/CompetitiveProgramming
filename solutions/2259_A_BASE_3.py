# https://jv.umsa.bo/oj/problem.php?cid=2826&pid=21
## https://jv.umsa.bo/oj/problem.php?id=2259
#  A BASE 3
#  Enviar
#  Estado
#  Descripción
#   Entrada
#   Salida
#    El resultado de convertir x a su equivalente en base 3
#   Ejemplo Entrada
#    4
#   Ejemplo Salida
#    11
#   Ayuda

def to_base3(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

N = int(input())
print(to_base3(N))