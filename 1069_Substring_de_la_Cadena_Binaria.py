# https://jv.umsa.bo/oj/problem.php?cid=2822&pid=3
## https://jv.umsa.bo/oj/problem.php?id=1069
#  Substring de la Cadena Binaria
#  Enviar
#  Estado
#  Descripción
#    El dia de hoy Reus se encontro con su profesor de algoritmos el cual le dio el siguiente problema.
#    Dado una cadena Binaria $S$ de longitud $N$ y $N$ siempre es par, Reus puede hacer la siguiente operacion las veces que desee.
#    Selecciona dos indices $i$ y $j$ donde $1 \leq i < j < N$, y $i$ y $j$ son posiciones impares.
#    Cambiar $S_i$ con $S_j$.
#    Cambiar $S_{i+1}$ con $S_{j+1}$.
#    Encontrar la maxima longitud de un substring no decreciente de la cadena $S$ luego de realizar cualquier numero (posiblemente cero) de operaciones.
#   Entrada
#    La primera linea contiene un entero $t$ $(1 \leq t \leq 10^4)$ que indica la cantidad de casos de prueba.
#    Cada caso de prueba consta de dos lineas de entrada.
#    La primera linea de cada caso de prueba contiene un entero $N$ $(2 \leq N \leq 2*10^5)$ donde $N$ es par y representa la longitud de la cadena binaria.
#    La siguiente linea contiene una cadena binaria $S$ de longitud $N$ donde cada $S_i$ es {0 o 1}.
#    La suma de $N$ sobre todos los casos de prueba no excedera $2*10^5$.
#   Salida
#    Para cada caso de prueba imprimir la maxima longitud de la subcadena no decreciente de la cadena que se puede obtener utilizando cualquier numero (posiblemente cero) de operaciones.
#   Ejemplo Entrada
#    3611000040110800100011
#   Ejemplo Salida
#    637
#   Ayuda
#    Para el primer caso de prueba tenemos $S=110000$, entonces elegimos $i=1$ y $j=5$ entonces obtendremos la cadena siguiente $S=000011$ entonces la longitud maxima de la subcadena no decreciente es 6.

