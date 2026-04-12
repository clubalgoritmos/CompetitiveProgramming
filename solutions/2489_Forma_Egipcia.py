# https://jv.umsa.bo/oj/problem.php?cid=2567&pid=10
#  Forma Egipcia
#  Estado
#  Descripción
#    Leonardo de Pisa, más conocido como Fibonacci, fue más reconocido por la secuencia que recibe su nombre. Sin embargo es el autor del primer algoritmo para escribir una fracción en forma Egipcia. La forma Egipcia consiste en escribir una fracción como la suma de fracciones donde el numerador es uno. Por ejemplo: $\frac{5}{6}=\frac{1}{2}+\frac{1}{3}$
#    El algoritmo escrito por Fibonacci es:
#    $\frac{x}{y}=\frac{1}{\lceil \frac{y}{x} \rceil}+\frac{-y \mod(x)}{y \lceil \frac{y}{x}\rceil}$
#    Luego se itera sobre la segunda fracción hasta conseguir que el numerador sea 1.
#    El problema consiste en escribir un programa que permita hallar la representación Egipcia de una fracción.
#   Entrada
#    El entrada consiste en múltiples casos de prueba. La primera linea indica el número de casos. Cada caso de prueba consiste en dos números enteros $x,y (x >y), (1 \leq x, y \leq 400)$ que representan el quebrado descrito.
#   Salida
#    En la salida escribe una línea representando la forma Egipcia como se muestra en el ejemplo. El orden es el que se genera al ejecutar el algoritmo.
#   Ejemplo Entrada
#    25 621 32
#   Ejemplo Salida
#    (1, 2) (1, 3)(1, 2) (1, 7) (1, 75) (1, 16800)
#   Ayuda

import math

def egyf(x, y):
    r = []
    while x != 0:
        z = math.ceil(y/x)
        r.append(z)
        x, y = -y % x, y * z
    return r

for _ in range(int(input())):
    x, y = map(int, input().split())
    f = egyf(x, y)
    print(" ".join(["(1, {})".format(i) for i in f]))