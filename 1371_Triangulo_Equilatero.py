# https://jv.umsa.bo/oj/problem.php?cid=2815&pid=1
#  Triangulo Equilatero
#  Enviar
#  Estado
#  Descripción
#    Le piden hallar la superficie de un triángulo equilatero.
#    para esto debera ingrear un numero entero e imprimir la superficie,
#   Entrada
#    Consiste de un numero entero.
#   Salida
#    Imprima en una linea el área de dicho triangulo.
#   Ejemplo Entrada
#    10
#   Ejemplo Salida
#    43.30
#   Ayuda

l = float(input())
print(f"{(3**.5)/4*l**2:.2f}")