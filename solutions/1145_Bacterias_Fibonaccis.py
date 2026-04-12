# https://jv.umsa.bo/oj/problem.php?id=1145
#  Bacterias Fibonaccis
#  Enviar
#  Estado
#  Descripción
#    La sucesión Fibonacci está relacionada con el crecimiento poblacional de conejos. Esta sucesión esta reflejada ahora de similar forma en el crecimiento poblacional de una nueva especie de bacteria que nació como experimento en los laboratorio OBI. El crecimiento está dado por año y cantidad de bacterias es decir año 1 cantidad 1, año 2 cantidad 1, año 3 cantidad 2 y así sucesivamente hasta llegar al año 200 donde se estima habrá 280571172992510140037611932413038677189525 de bacterias. Se te pide como programador calcular la cantidad de bacterias según tiempo transcurrido.
#   Entrada
#    La primera linea de entrada indica el numero de casos de prueba, cada caso se pueba indica el numero del año A y la cantidad de bacterias en dicho año. Asuma que 1<=A<=200.
#   Salida
#    La salida indica la cantidad de bacterias.
#   Ejemplo Entrada
#    712350100150200
#   Ejemplo Salida
#    112125862690253542248481792619150759969216677189303386214405760200280571172992510140037611932413038677189525
#   Ayuda

#bacterias fibonacci
f = []
for i in range(0, 201):
    f.append(0)


def fibo(n):
    if f[n] != 0:
        return f[n]
    if n < 2:
        return n
    else:
        f[n] = fibo(n - 1) + fibo(n - 2)
        return f[n]


m = int(input())
for i in range(0, m):
    print(fibo(int(input())))