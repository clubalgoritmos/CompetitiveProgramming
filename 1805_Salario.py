# https://jv.umsa.bo/oj/problem.php?id=1805
#  Salario
#  Enviar
#  Estado
#  Descripción
#    Obtener el sueldo neto y descuento provisional de un trabajador, conociendo su sueldo bruto. Si es un cargo administrativo se le descontará el 12% del sueldo bruto, y si es operativo se le descontará el 17%.
#    Obtener el sueldo neto y descuento provisional de un trabajador, conociendo su sueldo bruto. Si es un cargo administrativo se le descontará el 12% del sueldo bruto, y si es operativo se le descontará el 17%.
#   Entrada
#    La primera linbea de la entrada consiste en un numero entero que representa el n umero de casos.
#    Cada caso de prueba consiste de un numero entero y un numero entero que representa 1 si es administrativo y 2 si es operativo.
#   Salida
#    EL salarios que es un numero flotante con dos decimales
#   Ejemplo Entrada
#    25000 13200 2
#   Ejemplo Salida
#    4400.002656.00
#   Ayuda

n = int(input())
fun = lambda a, b: int(a)*0.88 if int(b)==1 else int(a)*0.83
for _ in range(n):
  a,b = map(int, input().split(" "))
  print('{:.2f}'.format(fun(a,b)))