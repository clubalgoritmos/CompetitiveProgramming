# https://jv.umsa.bo/oj/problem.php?id=1500
#  Array Palindrome?
#  Enviar
#  Estado
#  Descripción
#    Una cadena es palindrome si puede ser leida igual de atras hacia adelante y de adelante hacia atras.
#    Una cadena es palindrome si puede ser leida igual de atras hacia adelante y de adelante hacia atras.
#    Una cadena es palindrome si puede ser leida igual de atras hacia adelante y de adelante hacia atras.
#    La definicion de palidrome tambien se puede extender hacia arrays, para este problema te pedimos que verifiques si la secuencia de valores del array puede ser leida de la misma forma de atras hacia adelante y de adelante hacia atras.
#    La definicion de palidrome tambien se puede extender hacia arrays, para este problema te pedimos que verifiques si la secuencia de valores del array puede ser leida de la misma forma de atras hacia adelante y de adelante hacia atras.
#    La definicion de palidrome tambien se puede extender hacia arrays, para este problema te pedimos que verifiques si la secuencia de valores del array puede ser leida de la misma forma de atras hacia adelante y de adelante hacia atras.
#    Por ejemplo el array [$1$, $23$, $1$] es un array palindrome, pero el array [$123$, $3$, $21$] no lo es.
#    Por ejemplo el array [$1$, $23$, $1$] es un array palindrome, pero el array [$123$, $3$, $21$] no lo es.
#    Por ejemplo el array [$1$, $23$, $1$] es un array palindrome, pero el array [$123$, $3$, $21$] no lo es.
#   Entrada
#    En la primera linea de entrada un numero entero $n$ ($1 \leq n \leq 100$), el cual indica el tamaño del array $a$
#    En la primera linea de entrada un numero entero $n$ ($1 \leq n \leq 100$), el cual indica el tamaño del array $a$
#    En la primera linea de entrada un numero entero $n$ ($1 \leq n \leq 100$), el cual indica el tamaño del array $a$
#    En la segunda linea vendran los $n$ elementos del array $a$, donde $1 \leq a_{i} \leq 10^{5}$
#    En la segunda linea vendran los $n$ elementos del array $a$, donde $1 \leq a_{i} \leq 10^{5}$
#    En la segunda linea vendran los $n$ elementos del array $a$, donde $1 \leq a_{i} \leq 10^{5}$
#   Salida
#    Imprime SI si es que el array es palindrome y NOcaso contrario.
#    Imprime SI si es que el array es palindrome y NOcaso contrario.
#    Imprime SI si es que el array es palindrome y NOcaso contrario.
#   Ejemplo Entrada
#    51 32 23 32 1
#   Ejemplo Salida
#    SI
#   Ayuda

N = input()
A = list(map(int,input().split()))
if A==A[::-1]:
    print("SI")
    exit()
print("NO")