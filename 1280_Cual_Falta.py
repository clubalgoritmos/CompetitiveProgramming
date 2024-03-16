# https://jv.umsa.bo/oj/problem.php?id=1280
#  Cual Falta
#  Enviar
#  Estado
#  Descripción
#    Escriba un programa que lea secuencias con los números de $1$ a $n$ y diga cual numero falta.
#    Escriba un programa que lea secuencias con los números de $1$ a $n$ y diga cual numero falta.
#    Escriba un programa que lea secuencias con los números de $1$ a $n$ y diga cual numero falta.
#   Entrada
#    La entrada consiste de varias secuencias. Cada secuencia comienza con un numero $n$ entre $1$ y $1000$, seguida por $n$-$1$ números naturales. Cada numero aparece solo una vez, excepto uno que falta. La entrada termina cuando no hay más secuencias.
#    La entrada consiste de varias secuencias. Cada secuencia comienza con un numero $n$ entre $1$ y $1000$, seguida por $n$-$1$ números naturales. Cada numero aparece solo una vez, excepto uno que falta. La entrada termina cuando no hay más secuencias.
#    La entrada consiste de varias secuencias. Cada secuencia comienza con un numero $n$ entre $1$ y $1000$, seguida por $n$-$1$ números naturales. Cada numero aparece solo una vez, excepto uno que falta. La entrada termina cuando no hay más secuencias.
#   Salida
#    Para cada secuencia escriba el numero faltante.
#    Para cada secuencia escriba el numero faltante.
#    Para cada secuencia escriba el numero faltante.
#   Ejemplo Entrada
#    105 4 6 7 1 2 9 10 853 2 1 521
#   Ejemplo Salida
#    342
#   Ayuda
#    LECTURA DE MULTIPLES CASOS EN PYTHON O HASTA QUE NO HAYAN MAS DATOS
#    while True:   try:      #codigo   except EOFError:      break

while True:
    try:
        n = int(input())
        A = sorted(map(int,input().split()))
        for i in range(1,n+1):
            try:
                if i!=A[i-1]: raise Exception
            except:
                print(i)
                break
    except EOFError:
        break