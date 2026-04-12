# https://jv.umsa.bo/oj/problem.php?id=1822
#  TriPrimos
#  Enviar
#  Estado
#  Descripción
#    Beto el corcho sabe que los números primos son enteros positivos que tienen exactamente $2$ divisores positivos distintos. El decidió llamar a un entero positivo $t$ "ТRI-PRIMO", si $t$ tiene exactamente $3$ divisores positivos distintos.  Luego le dio a Paukis $n$-números y Paukis debe reconocer cuales son "TRI-PRIMOS", ayuda a Paukis para que no decepcione a Beto y no se ponga sad.
#    Beto el corcho sabe que los números primos son enteros positivos que tienen exactamente $2$ divisores positivos distintos. El decidió llamar a un entero positivo $t$ "ТRI-PRIMO", si $t$ tiene exactamente $3$ divisores positivos distintos.  Luego le dio a Paukis $n$-números y Paukis debe reconocer cuales son "TRI-PRIMOS", ayuda a Paukis para que no decepcione a Beto y no se ponga sad.
#    Beto el corcho sabe que los números primos son enteros positivos que tienen exactamente $2$ divisores positivos distintos. El decidió llamar a un entero positivo $t$ "ТRI-PRIMO", si $t$ tiene exactamente $3$ divisores positivos distintos.  Luego le dio a Paukis $n$-números y Paukis debe reconocer cuales son "TRI-PRIMOS", ayuda a Paukis para que no decepcione a Beto y no se ponga sad.
#   Entrada
#    La primera línea contiene un solo entero positivo $n$ $(1 \leq n \leq 10^5)$, el que indica cuántos números leer.
#    La primera línea contiene un solo entero positivo $n$ $(1 \leq n \leq 10^5)$, el que indica cuántos números leer.
#    La primera línea contiene un solo entero positivo $n$ $(1 \leq n \leq 10^5)$, el que indica cuántos números leer.
#    En las siguientes $n$ líneas contienen un número $x_i$$(1 \leq x_i \leq 10^{12})$ por línea.
#    En las siguientes $n$ líneas contienen un número $x_i$
#    En las siguientes $n$ líneas contienen un número $x_i$
#    $(1 \leq x_i \leq 10^{12})$ por línea.
#    $(1 \leq x_i \leq 10^{12})$ por línea.
#   Salida
#    Imprima n líneas: la línea $i$ -ésima debe imprimir "YES" (sin las comillas), si el número $x_i$ es ТRI-PRIMO, y "NO" (sin las comillas), si no lo es.
#    Imprima n líneas: la línea $i$ -ésima debe imprimir "YES" (sin las comillas), si el número $x_i$ es ТRI-PRIMO, y "NO" (sin las comillas), si no lo es.
#    Imprima n líneas: la línea $i$ -ésima debe imprimir "YES" (sin las comillas), si el número $x_i$ es ТRI-PRIMO, y "NO" (sin las comillas), si no lo es.
#   Ejemplo Entrada
#    33411
#   Ejemplo Salida
#    NOYESNO
#   Ayuda

for p in range(int(input())):
    num = int(input())
    div = list()
    for n in range(2, num):
        if num%n == 0:
            div.append(n)
    if len(div) == 1:
        print("YES")
    else:
        print("NO")