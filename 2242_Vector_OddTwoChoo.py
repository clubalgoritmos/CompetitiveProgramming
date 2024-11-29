# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=185
## https://jv.umsa.bo/oj/problem.php?id=2242
#    Copiado al portapapeles
#  Vector OddTwoChoo
#  Enviar
#  Estado
#  Descripción
#    Se pide que dado un número $n$ vamos a obtener un nuevo número $x_{i}$ de cada 2 dígitos adyacentes de este y preguntar si $x_{i}$ es impar, en caso de que un $x_{i}$ sea impar vamos a insertarlo en un vector $V$, luego ordenarlo ascendentemente y finalmente mostrarlo.
#    Ejemplo: si $n$ $\leftarrow$ $123435$ podemos obtener los siguientes números: $[35, 43, 34, 23, 12]$ de los cuales $[35, 43, 23]$ son impares.
#    NOTA: Esta garantizado que el vector $V$ tendrá al menos un número impar.
#   Entrada
#    Un número $t$ ($1 \leq t \leq 1500$) la cantidad de casos de entrada y en las siguientes $t$-líneas se leerá un número $n$ ($11 \leq n \leq 10^{18}$) el número del cual vamos a generar un vector $V$ por caso.
#   Salida
#    Se mostrará $t$-líneas, en cada línea se mostrara el vector generado de cada caso según lo que se pide en la descripción, cada 2 elementos de un vector tienen que estar separados por un espacio en blanco.
#   Ejemplo Entrada
#    31234561000237451222222221
#   Ejemplo Salida
#    23 452321 45 51
#   Ayuda
#    Ejemplo entrada 2:
#    12325654812325651
#    123435
#    10001
#    Ejemplo salida 2:
#    23 23 25 25 51 65 65 81
#    23 35 43
#    1

