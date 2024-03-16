# https://jv.umsa.bo/oj/problem.php?cid=2567&pid=0
#  Monótonos No Triviales Maximales
#  Estado
#  Descripción
#    Una secuencia de caracteres es no-trivial si contiene al menos dos elementos. Dada una secuencia s, decimosque el tramo si,...,sj es monótono si todos sus caracteres si son iguales, y decimos que es maximal si el tramono puede ser extendido hacia la izquierda o la derecha, perdiendo monotonicidad.
#    Una secuencia de caracteres es no-trivial si contiene al menos dos elementos. Dada una secuencia s, decimos
#    que el tramo si,...,sj es monótono si todos sus caracteres si son iguales, y decimos que es maximal si el tramo
#    no puede ser extendido hacia la izquierda o la derecha, perdiendo monotonicidad.
#    Dada una cadena compuesta únicamente por los caracteres "a" y "b", determine cuántas veces aparece elcaracter "a" en tramos monótonos maximales no-triviales. Por ejemplo, en la siguiente cadena:
#    Dada una cadena compuesta únicamente por los caracteres "a" y "b", determine cuántas veces aparece el
#    caracter "a" en tramos monótonos maximales no-triviales. Por ejemplo, en la siguiente cadena:
#    abababa
#    abababa
#    El resultado esperado es 0.
#    El resultado esperado es 0.
#    Otro ejemplo, en la siguiente cadena:
#    Otro ejemplo, en la siguiente cadena:
#    bbaababaaa
#    bbaababaaa
#    El resultado esperado es 5.
#    El resultado esperado es 5.
#   Entrada
#    La entrada consiste en una línea que contiene una cadena que consta únicamente de los caracteres "a" y "b".
#    La entrada consiste en una línea que contiene una cadena que consta únicamente de los caracteres "a" y "b".
#   Salida
#    Imprime una sola línea conteniendo un entero, representando el número de veces que aparece el
#    Imprime una sola línea conteniendo un entero, representando el número de veces que aparece el
#    caracter "a" en tramos monótonos maximales no-triviales.
#    caracter "a" en tramos monótonos maximales no-triviales.
#   Ejemplo Entrada
#    aababaaabb
#   Ejemplo Salida
#    5
#   Ayuda

secuence = list(input())
secuence.insert(0, "a")
secuence.append("a")
y = 0
for ab in range(1, len(secuence)-1):
    if secuence[ab] == "a" and (secuence[ab-1] == "a" or secuence[ab+1] == "a"):
        y = y+1
print(y)