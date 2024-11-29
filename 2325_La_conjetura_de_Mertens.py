# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=190
## https://jv.umsa.bo/oj/problem.php?id=2325
#    Copiado al portapapeles
#  La conjetura de Mertens
#  Enviar
#  Estado
#  Descripción
#    La conjetura de Mertens establece que $ M (n) $ está acotado por $ \ sqrt(n) $. Fue conjeturado por Thomas Joannes Stieltjes en una carta de 1885 a Charles Hermite y Franz Mertens (1897). No aprobaremos ni refutaremos esta conjetura, Andrew Odlyzko y Herman te Riele (1985) desaprobaron esta conjetura. La función de Mertens se define como:\[ M(n)=\sum _1^n \mu (k) \] Donde, para cualquier entero positivo n, define $ \mu(n) $ tiene valores en {-1, 0, 1} dependiendo de la factorización de n en factores primos:
#    n            1   2  3  4  5  6  7  8   9  10 Factorización  1    2    3    2*2  5   3*2   7  2*2*2  3*3   2*5 mu(n)          1   -1   -1    0   -1    1   -1   0      0     1
#    En la función $ \mu (n) $ podemos ver que 4,8,9 tiene un factor repetido, esa es la razón por la que $ \mu (n) $ es 0.
#   Entrada
#    La entrada consta de varios casos de prueba. Cada caso de prueba es el número $1 \leq n \leq10^6$ .La entrada termina cuando no hay más datos (fin de archivo)
#   Salida
#    Para cada impresión de caso de prueba:  \[ M(n)=\sum _1^n \mu (k) \]
#   Ejemplo Entrada
#    1020301000000
#   Ejemplo Salida
#    -1-3-3212
#   Ayuda

