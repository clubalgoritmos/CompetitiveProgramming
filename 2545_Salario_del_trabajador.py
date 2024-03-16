# https://jv.umsa.bo/oj/problem.php?id=2545
#  Salario del trabajador
#  Enviar
#  Estado
#  Descripción
#    A un trabajador se le paga de acuerdo a su salario por hora hasta 40 horas. Y por cada hora extra trabajada, se le incrementa solo el 50% del salario por hora. Escriba un programa que calcule el pago a un trabajador.
#   Entrada
#    La primera línea de entrada es un número entero t (t < 15), el cual indica cuantos casos de prueba se tiene en la entrada. Cada una de las siguientes t líneas, contiene dos enteros el número de horas (1 ≤ horas ≤ 100) y el salario por hora (1 ≤ salario ≤ 50).
#   Salida
#    Para cada línea de entrada se produce una línea de salida. Esta línea contiene el salario total, con dos decimales de precisión.
#   Ejemplo Entrada
#    141 30
#   Ejemplo Salida
#    1245.00
#   Ayuda

for _ in range(int(input())):
  h,sh = (int(x) for x in input().split(' '))
  a,r=0,0
  if h-40 >0:
    a = h-40
    r = a*sh*1.5
  r = (h-a)*sh + r
  print("{:.2f}".format(r))