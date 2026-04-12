# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=164
## https://jv.umsa.bo/oj/problem.php?id=1930
#    Copiado al portapapeles
#  Sin progresiones aritmeticas
#  Enviar
#  Estado
#  Descripción
#    Sea $f$ una secuencia de enteros positivos, con casos base $f(0) = 1$ y $f(1) = 1$.
#    Para cada $i \geq 2$, $f(i)$ es el menor entero positivo tal que para cualquier $k > 0$ y $i - 2k \geq 0$, tal que $f(i - 2k)$, $f(i - k)$ y $f(i)$ no es una progresion aritmetica.
#    Los primeros terminos de la secuencia son: $f(0) = 1$, $f(1) = 1$, $f(2) = 2$, $f(3) = 1$, $f(4) = 1$, $f(5) = 2$, $f(6) = 2$, $f(7) = 4$, $f(8) = 4$, etc.
#    $f(2)$ no puede ser 1, pues $f(0) = 1$, $f(1) = 1$, $f(2) = 1$ formarian una progresion aritmetica con $k=1$, por tanto $f(2) = 2$.
#    Tanto $f(3)$ y $f(4)$ no pueden formar progresiones aritmeticas con los terminos anteriores, por tanto su valor es 1.
#    $f(5)$ no puede ser 1, pues $f(3) = 1$, $f(4) = 1$, $f(5) = 1$ formarian una progresion aritmetica con $k=1$, por tanto $f(5) = 2$
#    $f(7)$ no puede ser 1, pues $f(1) = 1$, $f(3) = 1$, $f(7) = 1$ formarian una progresion aritmetica con $k=3$.
#    $f(7)$ no puede ser 2, pues $f(5) = 2$, $f(6) = 2$, $f(7) = 2$ formarian una progresion aritmetica con $k=1$.
#   Entrada
#    Un entero n($1 \leq n \leq 1000$).
#   Salida
#    Imprimir en una unica linea los primeros $n + 1$ terminos de la secuencia f.
#   Ejemplo Entrada
#    8
#   Ejemplo Salida
#    1 1 2 1 1 2 2 4 4
#   Ayuda

