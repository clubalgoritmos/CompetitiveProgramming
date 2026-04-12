# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=103
## https://jv.umsa.bo/oj/problem.php?id=1554
#    Copiado al portapapeles
#  La Subsecuencia ascendente más larga
#  Enviar
#  Estado
#  Descripción
#    La secuencia ascendente más larga se define como la secuencia más larga que podemos hallar quitando algunos elementos. Para solucionar este problema también utilizaremos programación dinámica. Por ejemplo sea la secuencia: ($10, 22, 9, 33, 21, 50, 41, 60, 80$). La secuencia ascendente más larga que podemos encontrar es de longitud $6$ y es ($10, 22, 33, 50, 60, 80$). Si vemos la secuencia ($6, 3, 5, 2, 7, 8, 1$) tenemos las siguientes secuencias:Subsecuencia no acendente: ($5, 2, 1$)Subsecuencia ascendente: ($3, 5, 9$)Subsecuencia ascendente: ($2, 7, 8$)La subsecuencia ascendente más larga: ($3, 5, 7, 8$)
#   Entrada
#    La entrada consiste de múltiples casos de prueba. Cada caso de prueba viene en dos líneas. La primera línea contiene el número $N \leq 10000$ de elementos de la secuencia. La siguiente línea tiene $N$ números enteros que son los elementos de la secuencia. La entrada termina cuando no hay más datos
#   Salida
#    Por cada caso de entrada escriba el tamaño de la subsecuencia ascendente más larga que se puede formar.
#   Ejemplo Entrada
#    910 22 9 33 21 50 41 60 8076 3 5 2 7 8 1
#   Ejemplo Salida
#    64
#   Ayuda

