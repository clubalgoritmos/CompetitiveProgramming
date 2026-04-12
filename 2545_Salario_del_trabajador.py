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

t = int(input())
for _ in range(t):
    horas, salario = map(int, input().split())
    pago = 0
    if horas <= 40:
        pago = horas * salario
    else:
        pago = 40 * salario + (horas - 40) * salario * 1.5

    print("{:.2f}".format(pago))  