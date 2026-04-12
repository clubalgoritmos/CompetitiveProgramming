# https://jv.umsa.bo/oj/problem.php?id=1327
#  Desproporción Diagonal
#  Enviar
#  Estado
#  Descripción
#    Se le ha encargado a usted calcular la desproporción diagonal de una matriz cuadrada. La desproporción diagonal de una matriz cuadradaes la suma de los elementos de su diagonal principal menos la suma de los elementos de la diagonal secundaria o colateral. La figura muestra la diagonal principal.
#    La figura muestra la diagonal secundaria.
#   Entrada
#    La entrada de datos consiste de varios casos de prueba. El primer número tiene el número de casos de prueba.Cada caso de prueba comienza con un número entero que tiene el número de filas de la matriz. Seguidamente vienen $N$ líneas, con la misma cantidad de caracteres, que contienen caracteres entre $0$ y $9$.
#   Salida
#    La salida es una línea por caso de prueba que tiene diferencia de las dos diagonales.
#   Ejemplo Entrada
#    43190828373  49000012000009000  1610 7748297018839541456770061997885446757413297249862805083967909986085827238606304156871895197729785238
#   Ejemplo Salida
#    1-10-24
#   Ayuda
#    guarde primero en variables el valor de las diagonales

for _ in range(int(input())):
    N = int(input())
    d1 = list()
    d2 = list()
    for i in range(N):
        s = input()
        d1.append(int(s[i]))
        d2.append(int(s[N-i-1]))
    print(sum(d1)-sum(d2))