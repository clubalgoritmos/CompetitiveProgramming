# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=19
## https://jv.umsa.bo/oj/problem.php?id=1132
#    Copiado al portapapeles
#  La Conjetura de Goldbach
#  Enviar
#  Estado
#  Descripción
#    En 1742, Christian Goldbach, un matemático alemán aficionado, envió una carta a Leonhard Euler, en el que hizo la siguiente conjetura:  Cada número mayor que 2 puede escribirse como la suma de tres números primos. Goldbach estaba considerando al 1 como un número primo, una convención que ya no se siguió.  Más tarde, Euler reiteró el conjeturas: Cada número aún mayor queo igual a 4 se puede expresar como la suma de dos números primos. Por ejemplo:
#    Hoy en día se sigue sin demostrarse si la conjetura es correcta. (Oh, espera, tengo la prueba, por supuesto, pero es demasiado tiempo para escribir en el margen de esta página).  Como tu eres un programador experimentado tu tarea es comprobar la conjetura de Goldbach según lo expresado por Euler para todos los números pares a menores a un millón.
#   Entrada
#    Cada caso de prueba consta de un entero de la forma $2k$, donde $3 \leq 2k \leq 1000000$
#   Salida
#    Imprimir una línea de la forma $n = a + b$, donde a y b son números primos impares. Los números y los operadores deben estar separados por exactamente un espacio en blancocomo en la salida de ejemplo a continuación. Si hay más de un par de números primos imparesañadir elegir el par donde la diferencia $b$ $-$ $a$ $sea maxima$.Si no hay dicho par, imprimir una línea que diga $"La conjetura$ $de$ $Goldbach$ $es$ $incorrecta."$
#   Ejemplo Entrada
#    82042
#   Ejemplo Salida
#    8 = 3 + 520 = 3 + 1742 = 5 + 37
#   Ayuda
#    Para el caso 3
#    42 = 5 + 37 tiene la diferencia máxima.
#    Se debe buscar todos los primos hasta n.

