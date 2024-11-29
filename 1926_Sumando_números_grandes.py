# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=161
## https://jv.umsa.bo/oj/problem.php?id=1926
#    Copiado al portapapeles
#  Sumando números grandes
#  Enviar
#  Estado
#  Descripción
#    Bob estaba aprendiendo teoría de números y se encontro con el siguiente problema:
#    Dado un conjunto $A$ de $N + 1$ números enteros, los cuales son: $$A = \{10 ^ {100}, 10 ^ {100} + 1, 10 ^ {100} + 2, ... , 10 ^ {100} + N - 1, 10 ^ {100} + N\}$$.
#    Definamos una función: $f(X) = y$, donde $X$ es un conjunto, $X\subseteq A$, e $y$, es el resultado de la suma de todos los números del conjunto $X$.
#    Formalmente se tiene:
#    $$f(X) = \displaystyle\sum_{i = 1} ^ {|X|} x_i$$
#    Donde:
#    $X = \{x_1, x_2, x_3, ... , x_{|X|}\}, X \subseteq A $
#    $|X|$, es el tamaño del conjunto $X$.
#    Tu puedes escoger $K$ o mas elementos de $A$. cuente todos los resultados posibles diferentes tomando $K$ o más elementos, usando la funcion $f(X)$, en otras palabras cuente los resultados diferentes de $f(R_i)$, donde $R_i$ esta en el rango $(K \leq R_i \leq N + 1)$.
#   Entrada
#    La primera linea de entrada tiene un número entero $t$, $(1 \leq t \leq 10)$, indicando los casos de prueba.
#    Luego vienen $t$ lineas, la $i$-ésima linea tiene dos enteros, $N_i$, $( 1 \leq N_i \leq 10 ^ 5)$, el tamaño del conjunto $A$, y$K_i$, $(1 \leq K_i \leq N_i + 1)$.
#    Luego vienen $t$ lineas, la $i$-ésima linea tiene dos enteros
#    , $N_i$, $( 1 \leq N_i \leq 10 ^ 5)$, el tamaño del conjunto $A$, y
#    $K_i$, $(1 \leq K_i \leq N_i + 1)$.
#   Salida
#    Imprima la cantidad de posibles resultados diferentes, como el resultado puede ser muy grande imprimir módulo $1000000007$.
#   Ejemplo Entrada
#    13 2
#   Ejemplo Salida
#    10
#   Ayuda
#    Los resultados diferentes del anterior ejemplo son los siguientes.
#    $(10 ^ {100}) + (10 ^ {100} + 1) = 2 * 10 ^ {100} + 1$.
#    $(10 ^ {100}) + (10 ^ {100} + 2) = 2 * 10 ^ {100} + 2$.
#    $(10 ^ {100}) + (10 ^ {100} + 3) = 2 * 10 ^ {100} + 3$.
#    $(10 ^ {100} + 3) + (10 ^ {100} + 1) = 2 * 10 ^ {100} + 4$.
#    $(10 ^ {100} + 2) + (10 ^ {100} + 3) = 2 * 10 ^ {100} + 5$.
#    $(10 ^ {100}) + (10 ^ {100} + 2) + (10 ^ {100} + 1) = 3 * 10 ^ {100} + 3$.
#    $(10 ^ {100}) + (10 ^ {100} + 3) + (10 ^ {100} + 1) = 3 * 10 ^ {100} + 4$.
#    $(10 ^ {100}) + (10 ^ {100} + 3) + (10 ^ {100} + 2) = 3 * 10 ^ {100} + 5$.
#    $(10 ^ {100} + 3) + (10 ^ {100} + 2) + (10 ^ {100} + 1) = 3 * 10 ^ {100} + 6$.
#    $(10 ^ {100}) + (10 ^ {100} + 2) + (10 ^ {100} + 3) + (10 ^ {100} + 1) = 4 * 10 ^ {100} + 6$.

