# https://jv.umsa.bo/oj/problem.php?cid=2823&pid=14
## https://jv.umsa.bo/oj/problem.php?id=1740
#  series dobles
#  Enviar
#  Estado
#  Descripción
#    Dando un numero generar:
#    -------1-------
#    ------222------
#    -----33333-----
#    ----4444444----
#    ---555555555---
#    --66666666666--
#    -7777777777777-
#   Entrada
#    Un numero mayor a cero
#   Salida
#    N líneas
#   Ejemplo Entrada
#    3
#   Ejemplo Salida
#    ---1-----222---33333-
#   Ayuda

N = int(input())
for i in range(1, N+1):
    print(f"{'-'*(N-i+1)}{str(i)*(2*i-1)}{'-'*(N-i+1)}")
