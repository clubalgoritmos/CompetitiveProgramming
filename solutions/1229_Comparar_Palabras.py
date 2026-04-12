# https://jv.umsa.bo/oj/problem.php?id=1229
#  Comparar Palabras
#  Enviar
#  Estado
#  Descripción
#    Escriba un programa que lea dos palabras e imprima el signo < (menor que), > (mayor que) o = (igual que) de acuerdo al orden lexicógrafo.
#    <
#    >
#    =
#   Entrada
#    La entrada consiste de dos palabras a, b con caracteres en minúsculas, en una sola linea, separadas por un espacio.
#    a
#    b
#   Salida
#    Imprima una linea indicando si a < b, a > b o a = b.
#    a < b
#    a > b
#    a = b
#   Ejemplo Entrada
#    anna xavier
#   Ejemplo Salida
#    anna < xavier
#   Ayuda

a, b = input().split()
if a>b:
    print(f"{a} > {b}")
elif a<b:
    print(f"{a} < {b}")
else:
    print(f"{a} = {b}")