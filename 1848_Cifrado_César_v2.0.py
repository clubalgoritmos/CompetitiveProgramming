# https://jv.umsa.bo/oj/problem.php?id=1848
#  Cifrado César v2.0
#  Enviar
#  Estado
#  Descripción
#    El cifradoCésarmueve cada letra un determinado número de espacios en el alfabeto. En esta versión, necesitamos tener un valor de desplazamiento, que se calculará en cada palabra, contando el caracter que más veces se repita.
#    El cifrado
#    mueve cada letra un determinado número de espacios en el alfabeto. En esta versión, necesitamos tener un valor de desplazamiento, que se calculará en cada palabra, contando el caracter que más veces se repita.
#    Por ejemplo, si la palabra fuera ANA, su clave de desaplazamiento sería 2, porque hay una letra A que se repite 2 veces. Si la palabra fuera SOL, su clave de desplazamiento sería 1, porque todas las letras se repiten una sola vez. Ysi la palabra fuera ENTENDISTE, su clave de desplazamiento sería 3, porque la E se repite 3 veces.
#    Por ejemplo, si la palabra fuera ANA, su clave de desaplazamiento sería 2, porque hay una letra A que se repite 2 veces. Si la palabra fuera SOL, su clave de desplazamiento sería 1, porque todas las letras se repiten una sola vez. Y
#    Utilicemos la siguiente tabla de conversión:
#    La nueva palabra codificada, empieza por la clave de desplazamiento. En el caso de ANA, la clave era 2, que equivale según la imagen a la letra B, luego empezamos a codificar el texto original, tomando su posición e incrementando la clave de desplazamiento, tendremos la siguiente letra, en el caso de ANA sería: A = 1 + 2 = 3 = C, N = 14 + 2 = 16 = O, A = 1 + 2 = 3 = C
#    Por tanto el texto cifrado será (todas las negrillas): BCOC
#   Entrada
#    La entrada consiste de varios casos de prueba. Cada caso de prueba comienza con un número natural k >0, seguido de k cadenas, una cadena por línea,de sólo letras mayúsculas.
#    La entrada consiste de varios casos de prueba. Cada caso de prueba comienza con un número natural k >0
#    k >0
#    , seguido de k cadenas, una cadena por línea,
#    de sólo letras mayúsculas.
#   Salida
#    Para cada caso de prueba escriba una línea con el texto cifrado en mayúsculas. En caso de que el texto original contenga números, o caracteres especiales, solamente vuelvalos a repetir.
#    Para cada caso de prueba escriba una línea con el texto cifrado en mayúsculas. En caso de que el texto original contenga números, o caracteres especiales, solamente vuelvalos a repetir.
#   Ejemplo Entrada
#    5HAYMOMENTOSENLAVIDA
#   Ejemplo Salida
#    AIBZBÑQÑGOVQUAFÑAMBAWJEB
#   Ayuda

for _ in range(int(input())):
  a = input().upper()
  p = list(set(a))
  c = 0
  for x in p:
    if a.count(x) > c:
      c = a.count(x)
  abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
  r = ""
  r = r + abc[c-1]
  for x in a:
    r = r + abc[abc.find(x)+c]
  print(r)