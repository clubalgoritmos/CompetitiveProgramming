# https://jv.umsa.bo/oj/problem.php?id=1333
#  Easy Suffix Array
#  Enviar
#  Estado
#  Descripción
#    En Ciencias de la Computación un arreglo de sufijos es un arreglo ordenado de todos los sufijos de una cadena dada. Esta estructura de datos es muy simple, pero sin embargo es muy poderosa y es usada en algoritmos de compresión de datos y dentro del campo de la bioinformática , indización de textos completos, entre otros.Por ejemplo dada la cadena "banana" los sufijos de esta cadena son:
#    Y si los ordenamos lexicograficamente tendriamos:
#    El array {"a", "ana", "anana", "banana", "na", "nana"} seria el suffix array de la cadena "banana".Te pedimos obtener el suffix array de una cadena dada en la entrada, existen algoritmos muy eficientes para obtener el suffix array de una cadena pero en esta ocasión no estamos interesados en ellos.
#   Entrada
#    Una sola cadena $S$ sin espacios de longitud $N$ ($1 <= N <= 100$). La cadena solo consta de letras minusculas.
#   Salida
#    N cadenas, una cadena en cada linea, las cuales representan el suffix array de la cadena de la entrada.
#   Ejemplo Entrada
#    banana
#   Ejemplo Salida
#    aanaananabananananana
#   Ayuda
#    La función compareTo para cadenas(tipo de variables String) de Java compara lexicograficamente.

S = input()
print(*sorted([S[i:] for i in range(len(S))]), sep="\n")