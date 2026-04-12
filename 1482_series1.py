# https://jv.umsa.bo/oj/problem.php?id=1482
#  series1
#  Enviar
#  Estado
#  Descripción
#    Juan es un chico muy brillante al cual se le presento un problema curioso el esta acostumbrado a resolver planteamientos con dato enteros positivos ante la existencia de signos negativos el se desanima ayuda a juan a generar la siguiente serie de números hasta $n (-1, 2, -6, 24, -120)$
#   Entrada
#    La entrada consiste en un número $n$ leido por teclado
#   Salida
#    Se debe mostrar los elementos generados de la serie hasta $n$
#   Ejemplo Entrada
#    5
#   Ejemplo Salida
#    -12-624-120
#   Ayuda
#    Considere que el signo cambia y que la serie crece rapidamente para esto almacenar los números en un int podría no ser suficiente

n = int(input())
serie = [1,2,6,24,120]

def generate_serie(n):
    if n<len(serie):
        return serie[n]
    else:
        serie.append(serie[n-1]*(n-1))
        return serie[n]

for i in range(n):
    print(int(generate_serie(i)*(-1)**(i-1)))