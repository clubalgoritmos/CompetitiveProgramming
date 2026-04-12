# https://jv.umsa.bo/oj/problem.php?id=2414
#  Tuncuña Lineal
#  Enviar
#  Estado
#  Descripción
#    Julio ve a su hermano menor Pedrito jugando a la Tuncuña. El está entusiasmado con lo interesante del juego, y decidió jugarlo también. Se pinta una secuencia de cuadrados en el suelo con la ayuda de una tiza, y se le asigna un número a cada cuadrado (1, 2, 3, 4, ...). Julio se ubica al principio de esos cuadrados. A partir de aquí, lanza una piedrita al primer cuadrado, entonces Julio se mueve a ese cuadrado, recoge la piedrita, y vuelve a lanzar la piedrita pero esta vez 2 cuadrados adelante, se mueve a ese cuadrado y recoge la piedrita, y vuelve a lanzar la piedrita, pero esta vez 3 cuadrados adelante, y así sucesivamente.
#    Julio ve a su hermano menor Pedrito jugando a la Tuncuña. El está entusiasmado con lo interesante del juego, y decidió jugarlo también. Se pinta una secuencia de cuadrados en el suelo con la ayuda de una tiza, y se le asigna un número a cada cuadrado (1, 2, 3, 4, ...). Julio se ubica al principio de esos cuadrados. A partir de aquí, lanza una piedrita al primer cuadrado, entonces Julio se mueve a ese cuadrado, recoge la piedrita, y vuelve a lanzar la piedrita pero esta vez 2 cuadrados adelante, se mueve a ese cuadrado y recoge la piedrita, y vuelve a lanzar la piedrita, pero esta vez 3 cuadrados adelante, y así sucesivamente.
#    ¿Cuál es el objetivo del juego? El objetivo es comprobar si es posible llegar al N-ésimo cuadrado con el procedimiento descrito. Además, Julio es un poco perezoso. El jugará solamente si está seguro de que puede llegar al N-ésimo cuadrado. Ayuda a Julio a decidir si jugará o no.
#    ¿Cuál es el objetivo del juego? El objetivo es comprobar si es posible llegar al N-ésimo cuadrado con el procedimiento descrito. Además, Julio es un poco perezoso. El jugará solamente si está seguro de que puede llegar al N-ésimo cuadrado. Ayuda a Julio a decidir si jugará o no.
#   Entrada
#    La primera línea contiene un número entero T (1≤T≤100), que indica el número de veces que Julio jugará el juego. Cada una de las T siguientes líneas contiene un único entero N (1≤N≤1000), que denota el N-ésimo cuadrado.
#    La primera línea contiene un número entero T (1≤T≤100), que indica el número de veces que Julio jugará el juego. Cada una de las T siguientes líneas contiene un único entero N (1≤N≤1000), que denota el N-ésimo cuadrado.
#   Salida
#    La salida se compone de varias líneas (una línea por cada caso de prueba), siguiendo los siguientes criterios:
#    La salida se compone de varias líneas (una línea por cada caso de prueba), siguiendo los siguientes criterios:
#    · Si Julio es capaz de llegar al N-ésimo cuadrado, entonces imprime "Llegas al cuadrado " (sin comillas) seguido del número de movimientos necesarios para llegar al N-ésimo cuadrado, ambos separados por un espacio.
#    ·
#    Si Julio es capaz de llegar al N-ésimo cuadrado, entonces imprime "
#    " (sin comillas) seguido del número de movimientos necesarios para llegar al N-ésimo cuadrado, ambos separados por un espacio.
#    · Si Julio no es capaz de llegar al N-ésimo cuadrado, imprime "No llegas" (sin comillas).
#    ·
#    Si Julio no es capaz de llegar al N-ésimo cuadrado, imprime "
#    " (sin comillas).
#   Ejemplo Entrada
#    3236
#   Ejemplo Salida
#    No llegasLlegas al cuadrado 2Llegas al cuadrado 3
#   Ayuda

for _ in range(int(input())):
  n = int(input())
  i, x = 1, 1
  while x<n:
    i+=1
    x+=i
  if x==n:
    print(f"Llegas al cuadrado {i}")
  else:
    print("No llegas")