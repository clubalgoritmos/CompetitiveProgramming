# https://jv.umsa.bo/oj/problem.php?id=1807
#  Número especial
#  Enviar
#  Estado
#  Descripción
#    Mike se encontraba en clases de matemáticas con un profesor sumamente aburrido y , uno de esos momentos, se le ocurrió un juego extraño que consistía en que cada vez que veía un número de varios dígitos en su libro de matemáticas quería averiguar si era un número especial.
#    Mike se encontraba en clases de matemáticas con un profesor sumamente aburrido y , uno de esos momentos, se le ocurrió un juego extraño que consistía en que cada vez que veía un número de varios dígitos en su libro de matemáticas quería averiguar si era un número especial.
#    Un número es especial cuando este tiene dígitos conformados, solamente, por el número cuatro y/o el número siete, o bien, era múltiplo de cuatro o era múltiplo de siete.Por ejemplo: 192 es un número especial por que es múltiplo de 4 y 477 es una secuencia de 4 y 7, por lo tanto, es un número especialTu tarea es realizar un programa que indique si el número que Mike ve en su libro es un número especial.
#    Un número es especial cuando este tiene dígitos conformados, solamente, por el número cuatro y/o el número siete, o bien, era múltiplo de cuatro o era múltiplo de siete.Por ejemplo: 192 es un número especial por que es múltiplo de 4 y 477 es una secuencia de 4 y 7, por lo tanto, es un número especialTu tarea es realizar un programa que indique si el número que Mike ve en su libro es un número especial.
#    Un número es especial cuando este tiene dígitos conformados, solamente, por el número cuatro y/o el número siete, o bien, era múltiplo de cuatro o era múltiplo de siete.
#    Un número es especial cuando este tiene dígitos conformados, solamente, por el número cuatro y/o el número siete, o bien, era múltiplo de cuatro o era múltiplo de siete.
#    Por ejemplo: 192 es un número especial por que es múltiplo de 4 y 477 es una secuencia de 4 y 7, por lo tanto, es un número especial
#    Por ejemplo: 192 es un número especial por que es múltiplo de 4 y 477 es una secuencia de 4 y 7, por lo tanto, es un número especial
#    Tu tarea es realizar un programa que indique si el número que Mike ve en su libro es un número especial.
#    Tu tarea es realizar un programa que indique si el número que Mike ve en su libro es un número especial.
#   Entrada
#    La entrada consiste en varios casos de pueba, cada caso de prueba tiene una simple línea, un numero entero n (1<=n<=1000), la secuencia de números que se necesita revisar.
#    La entrada consiste en varios casos de pueba, cada caso de prueba
#    tiene una simple línea, un numero entero n (1<=n<=1000), la secuencia de números que se necesita revisar.
#   Salida
#    La salida son varias líneas que diga “YES” si la secuencia n es un número especial, de lo contrario imprimir “NO”.
#    La salida son varias líneas que diga “YES” si la secuencia n es un número especial, de lo contrario imprimir “NO”.
#    La salida son varias líneas que diga “YES” si la secuencia n es un número especial, de lo contrario imprimir “NO”.
#   Ejemplo Entrada
#    19247713
#   Ejemplo Salida
#    YESYESNO
#   Ayuda

import sys
for i in sys.stdin:
  n = int(i)
  if (n%4==0 or n%7==0) or (set(map(int, str(n)))=={4,7}):
    print("YES")
  else:
    print("NO")