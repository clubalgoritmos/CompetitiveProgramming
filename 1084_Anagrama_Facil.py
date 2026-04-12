# https://jv.umsa.bo/oj/problem.php?id=1084
#  Anagrama Facil
#  Enviar
#  Estado
#  Descripción
#    Un Anagrama es una palabra o frase que resulta de la transposición de letras de otra palabra o frase. Por ejemplo: AMOR - ROMA - OMAR - MORA - RAMO - ARMO - MARO, todas son anagramas. Este problema es complejo cuando la cantidad de caracteres crece.  En esta ocasión se trata de un problema más reducido, en el que se tiene un diccionario de palabras y se quiere saber de cada palabra cuántos anagramas se tiene en el diccionario.  Por ejemplo, si se tiene el diccionario: cava, empresa, pote, torta, tope, trota, vaca. La palabra\cava tiene un anagrama que seria vaca y viceversa. Entonces la respuesta correcta sería: 1, 0, 1, 1, 1, 1, 1. En este caso particular la palabra empresa no tiene anagramas.
#   Entrada
#    La entrada consiste de un número entero positivo c que indica la cantidad de casos que se deben probar. Por cada caso de prueba, se tiene un número entero positivo n, (1 < n < 100000), y una secuencia de n cadenas que son las palabras del diccionario. Todas las cadenas están escritas en minúscula y cada caracter de las palabras está en el rango [`a', `z'].
#   Salida
#    Para cada caso de prueba se debe emitir en una linea una secuencia de números separados por un espacio en blanco que indiquen la cantidad de anagramas que tiene cada palabra en el diccionario.
#   Ejemplo Entrada
#    27cavaempresapotetortatopetrotavaca6arooraalocolaolaloa
#   Ejemplo Salida
#    1 0 1 1 1 1 11 1 2 0 2 2
#   Ayuda

for _  in range(int(input())):
    N = int(input())
    v = {input():0 for _ in range(N)}
    for k in v:
        v[k] = sum([1 for i in v if sorted(i)==sorted(k)])-1
    print(*v.values())