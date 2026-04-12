# https://jv.umsa.bo/oj/problem.php?id=2300
#  Alice y Bob
#  Enviar
#  Estado
#  Descripción
#    Alice y Bob estudian en la misma escuela, como el profesor no llegaba, pues los estudiantes se empezaron a aburrir, pero Alice noto algo interesante en las mesas de su curso
#    Alice y Bob estudian en la misma escuela, como el profesor no llegaba, pues los estudiantes se empezaron a aburrir, pero Alice noto algo interesante en las mesas de su curso
#    Alice y Bob estudian en la misma escuela, como el profesor no llegaba, pues los estudiantes se empezaron a aburrir, pero Alice noto algo interesante en las mesas de su curso
#    Como se puede ver, las mesas tienen una forma de matriz, asi que se le ocurrio el siguiente juego, y le reto a Bob.
#    Como se puede ver, las mesas tienen una forma de matriz, asi que se le ocurrio el siguiente juego, y le reto a Bob.
#    Como se puede ver, las mesas tienen una forma de matriz, asi que se le ocurrio el siguiente juego, y le reto a Bob.
#    Bob debera posicionarse en la posicion $A_{0,0}$, parte superior izquierda de la matriz, luego Alice pone una Mochila con comida en una mesa, que estara representada por la letra 'C', asi que Bob para llegar a esa mesa, solo puede hacer saltos entre mesas, pero solo pueder saltar a la derecha o a abajo.
#    Bob debera posicionarse en la posicion $A_{0,0}$, parte superior izquierda de la matriz, luego Alice pone una Mochila con comida en una mesa, que estara representada por la letra 'C', asi que Bob para llegar a esa mesa, solo puede hacer saltos entre mesas, pero solo pueder saltar a la derecha o a abajo.
#    Bob debera posicionarse en la posicion $A_{0,0}$, parte superior izquierda de la matriz, luego Alice pone una Mochila con comida en una mesa, que estara representada por la letra 'C', asi que Bob para llegar a esa mesa, solo puede hacer saltos entre mesas, pero solo pueder saltar a la derecha o a abajo.
#    Lastimosamente Bob por llegar temprano a clases, no desayuno, y como vino caminando a la escuela pues gasto parte de la energia que tiene, asi que Bob solo tiene energia $k$ y en cada salto Bob gasta uno de energia, ademas Bob se dio cuenta que algunas mesas estan en mal estado, asi que no puede saltar sobre ellas.
#    Lastimosamente Bob por llegar temprano a clases, no desayuno, y como vino caminando a la escuela pues gasto parte de la energia que tiene, asi que Bob solo tiene energia $k$ y en cada salto Bob gasta uno de energia, ademas Bob se dio cuenta que algunas mesas estan en mal estado, asi que no puede saltar sobre ellas.
#    Lastimosamente Bob por llegar temprano a clases, no desayuno, y como vino caminando a la escuela pues gasto parte de la energia que tiene, asi que Bob solo tiene energia $k$ y en cada salto Bob gasta uno de energia, ademas Bob se dio cuenta que algunas mesas estan en mal estado, asi que no puede saltar sobre ellas.
#    Bob empezo a preguntarse si puede llegar a la mesa con la energia que le queda, solo Bob aceptara el reto si es que puede llegar a la mesa indicada y comer para tener mas energia, caso contrario no aceptara el reto ya que se quedara sin energia y no podra volver a casa, asi que como Bob sabe que tu eres un buen programador, te pide ayuda para que le puedas decir si el tiene que aceptar el reto o no
#    Bob empezo a preguntarse si puede llegar a la mesa con la energia que le queda, solo Bob aceptara el reto si es que puede llegar a la mesa indicada y comer para tener mas energia, caso contrario no aceptara el reto ya que se quedara sin energia y no podra volver a casa, asi que como Bob sabe que tu eres un buen programador, te pide ayuda para que le puedas decir si el tiene que aceptar el reto o no
#    Bob empezo a preguntarse si puede llegar a la mesa con la energia que le queda, solo Bob aceptara el reto si es que puede llegar a la mesa indicada y comer para tener mas energia, caso contrario no aceptara el reto ya que se quedara sin energia y no podra volver a casa, asi que como Bob sabe que tu eres un buen programador, te pide ayuda para que le puedas decir si el tiene que aceptar el reto o no
#   Entrada
#    La entrada tiene varios casos de prueba.
#    La entrada tiene varios casos de prueba.
#    La entrada tiene varios casos de prueba.
#    Cada caso tiene lo siguiente:
#    Cada caso tiene lo siguiente:
#    Cada caso tiene lo siguiente:
#    La primera linea tiene $3$ numeros enteros $n, m, k$, ($ 1 \leq n, m \leq 8$), $n$ significa que hay $n$ filas de mesas y en cada fila hay $m$ mesas, y $k$ ($ 1 \leq k \leq 100$), que indica la energia de Bob en ese momento.
#    La primera linea tiene $3$ numeros enteros $n, m, k$, ($ 1 \leq n, m \leq 8$), $n$ significa que hay $n$ filas de mesas y en cada fila hay $m$ mesas, y $k$ ($ 1 \leq k \leq 100$), que indica la energia de Bob en ese momento.
#    La primera linea tiene $3$ numeros enteros $n, m, k$, ($ 1 \leq n, m \leq 8$), $n$ significa que hay $n$ filas de mesas y en cada fila hay $m$ mesas, y $k$ ($ 1 \leq k \leq 100$), que indica la energia de Bob en ese momento.
#    Luego vienen $n$ lineas, cada linea tiene $m$ caracteres.
#    Luego vienen $n$ lineas, cada linea tiene $m$ caracteres.
#    Luego vienen $n$ lineas, cada linea tiene $m$ caracteres.
#    '.' significa que la mesa esta en buen estado
#    '.' significa que la mesa esta en buen estado
#    '#' significa que la mesa esta en mal estado
#    '#' significa que la mesa esta en mal estado
#    'C' significa que en esa mesa esta la mochila c
#    'C' significa que en esa mesa esta la mochila c
#    on comida que puso Alice
#    on comida que puso Alice
#    Se garantiza que la mesa $A_{0,0}$, siempre esta en buen estado
#    Se garantiza que la mesa $A_{0,0}$, siempre esta en buen estado
#    Se garantiza que la mesa $A_{0,0}$, siempre esta en buen estado
#   Salida
#    Para cada caso de prueba, muestre lo siguiete:
#    Para cada caso de prueba, muestre lo siguiete:
#    Para cada caso de prueba, muestre lo siguiete:
#    "Intentalo Bob" si Bob podrá llegar a la mochila con comida
#    "Intentalo Bob" si Bob podrá llegar a la mochila con comida
#    "Descansa Bob" si Bob no podrá llegar a la mochila con comida
#    "Descansa Bob" si Bob no podrá llegar a la mochila con comida
#   Ejemplo Entrada
#    3 4 4...#..#.#.C.
#   Ejemplo Salida
#    Intentalo Bob
#   Ayuda
#    Si Bob sigue la siguiente Ruta: ADAD o DAAD, con cualquiera de las $2$ rutas, Bob puede llegar a la mochila con comida
#    Si Bob sigue la siguiente Ruta: ADAD o DAAD, con cualquiera de las $2$ rutas, Bob puede llegar a la mochila con comida
#    Si Bob sigue la siguiente Ruta: ADAD o DAAD, con cualquiera de las $2$ rutas, Bob puede llegar a la mochila con comida

intext = input()
intable = intext.split(" ")
print = (intable)