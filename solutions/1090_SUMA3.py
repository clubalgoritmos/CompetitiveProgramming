# https://jv.umsa.bo/oj/problem.php?id=1090
#  SUMA3
#  Enviar
#  Estado
#  Descripción
#    La suma3 es la suma de los números inferiores a un número dado (empezando del 1), pero que sean múltiplos de 3.
#    Por ejemplo si el número es 10 la suma3 será 3+6+9=18 puesto que 3,6,y 9 son inferiores a 10 y además son múltiplos de 3.
#   Entrada
#    Se ingresará un número n por el teclado (1<=n<=10000).
#   Salida
#    Se debe imprimir la suma3 en una línea.
#   Ejemplo Entrada
#    9
#   Ejemplo Salida
#    9
#   Ayuda

n = int(input())
S = 0
for i in range(3,n, 3):
 S=S+i
print(S)