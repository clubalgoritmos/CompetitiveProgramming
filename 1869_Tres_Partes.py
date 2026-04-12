# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=154
## https://jv.umsa.bo/oj/problem.php?id=1869
#    Copiado al portapapeles
#  Tres Partes
#  Enviar
#  Estado
#  Descripción
#    Se le proporciona un arreglo $d_{1}, d_{2}, ..., d_{n}$ que consta de n números enteros.
#    Su tarea es dividir este arreglo en tres partes (algunas de las cuales pueden estar vacías) de tal manera que cada elemento del arreglo pertenezca exactamente a una de las tres partes, y cada una de las partes forma un subsegmento contiguo consecutivo (posiblemente, vacío) del arreglo original.
#    Sea la suma de elementos de la primera parte sum1, la suma de elementos de la segunda parte sum2 y la suma de elementos de la tercera parte sum3. Entre todas las formas posibles de dividir la matriz, debe elegir una forma tal que sum1 = sum3 y sum1 sea lo máximo posible.
#    Más formalmente, si la primera parte de la arreglo contiene a elementos, la segunda parte del arreglo contiene b elementos y la tercera parte contiene c elementos, entonces:
#    \[sum1 = \sum_{1 \leq i \leq a} d_{i}\]
#    \[sum2 = \sum_{a+1 \leq i \leq a+b} d_{i}\]
#    \[sum3 = \sum_{a+b+1 \leq i \leq a+b+c} d_{i}\]
#    La suma de un arreglo vacío es 0.
#    Su tarea es encontrar una manera de dividir el arreglo de manera que sum1 = sum3 y sum1 sea lo máximo posible.
#   Entrada
#    La entrada consiste en multiples casos de prueba. La primera linea contiene un entero T, que representa el numero casos de entrada, para cada caso de entrada un número entero n $(1 \leq n \leq 10^5)$: el número de elementos en el arreglo d.
#    seguido n enteros $d_{1}, d_{2}, ..., d_{n}$ donde $(1 \leq d_{i} \leq 10^9)$, los elementos del arreglo d.
#   Salida
#    Imprima un número entero único: el valor máximo posible de sum1, considerando que se debe cumplir la condición sum1 = sum3.
#    Obviamente, existe al menos una forma válida de dividir la matriz (use a = c = 0 y b = n).
#   Ejemplo Entrada
#    351 3 1 1 451 3 2 1 434 1 2
#   Ejemplo Salida
#    540
#   Ayuda
#    En el primer ejemplo, solo hay una división posible que maximiza es sum1 = 5: [1,3,1], [], [1,4].
#    En el segundo ejemplo, la única forma de tener sum1 = 4: [1,3], [2,1], [4].
#    En el tercer ejemplo, solo hay una forma de dividir el arreglo sum1 = 0: [], [4,1,2], [].

