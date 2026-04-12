# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=219
## https://jv.umsa.bo/oj/problem.php?id=2551
#    Copiado al portapapeles
#  INDICE DE PALABRAS
#  Enviar
#  Estado
#  Descripción
#    Los esquemas de codificación a menudo se utilizan en situaciones que requieren encriptación o almacenamiento/transmisión de información. Aquí, desarrollamos un esquema de codificación simple que codifica tipos particulares de palabras con cinco letras o menos en minúsculas como enteros.Consideremos el alfabeto inglés {a,b,c,...,z}. Usando este alfabeto, se deben formar un conjunto de palabras válidas que estén en un estricto orden lexicográfico. En este conjunto de palabras válidas, las letras sucesivas de una palabra están en un orden estrictamente ascendente; es decir, las letras posteriores en una palabra válida siempre están después de las letras anteriores con respecto a sus posiciones en la lista alfabética {a,b,c,...,z}. Por ejemplo,abc aep gwzson todas palabras válidas de tres letras, mientras queaab are catno lo son.Para cada palabra válida se le asigna un entero que indica la posición de la palabra en la lista alfabética de palabras. Es decir:a -> 1b -> 2..z -> 26ab -> 27ac -> 28..az -> 51bc -> 52..vwxyz -> 83681Su programa debe leer una serie de líneas de entrada. Cada línea de entrada tendrá una sola palabra, que tendrá entre una y cinco letras. Para cada palabra leída, si la palabra no es válida, dé el número '0'. Si la palabra leída es válida, dé el índice de posición de la palabra en la lista alfabética anterior.
#   Entrada
#    La entrada consiste en una serie de palabras individuales, una por línea. Las palabras tienen al menos una letra y no más de cinco letras. Solo se utilizarán caracteres alfabéticos minúsculos {a,b,...,z} como entrada. La primera letra de una palabra aparecerá como el primer carácter en una línea de entrada. La entrada finalizará con el fin del archivo.
#   Salida
#    La salida es un solo entero, mayor o igual a cero (0) y menor o igual a 83681. El primer dígito de un valor de salida debe ser el primer carácter en una línea. Hay una línea de salida para cada línea de entrada
#   Ejemplo Entrada
#    zacatvwxyz
#   Ejemplo Salida
#    261083681
#   Ayuda

