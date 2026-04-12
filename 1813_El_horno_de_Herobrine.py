# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=147
## https://jv.umsa.bo/oj/problem.php?id=1813
#    Copiado al portapapeles
#  El horno de Herobrine
#  Enviar
#  Estado
#  Descripción
#    Herobrine es un jugador en el famoso mundo de Minecraft, y tiene un horno bastante peculiar. En un horno normal se pueden utilizar hasta nueve ingredientes y el tiempo de preparación de un alimento no varía. En el horno especial de Herobrine no es así.
#    El horno de Herobrine cocina los ingredientes uno por uno, no puede exceder la capacidad de h gramos de alimento, y sólo cocina k gramos de un solo alimento cada segundo. Si hay menos de k gramos restantes de un mismo alimento, cocina solamente esa cantidad restante utilizando un segundo.
#    El horno de Herobrine cocina los ingredientes uno por uno, no puede exceder la capacidad de
#    h
#    gramos de alimento, y sólo cocina
#    k
#    gramos de un solo alimento cada segundo. Si hay menos de k gramos restantes de un mismo alimento, cocina solamente esa cantidad restante utilizando un segundo.
#    Herobrine tiene n piezas de materiales para cocinar, el peso de la i-ésima pieza es igual a ai. Él coloca en el horno los materiales uno por uno empezando del material 1 hasta el material n.
#    Herobrine tiene
#    n
#    piezas de materiales para cocinar, el peso de la i-ésima pieza es igual a a
#    i
#    . Él coloca en el horno los materiales uno por uno empezando del material 1 hasta el material
#    .
#    Cada segundo, ocurre lo siguiente:
#    1. Si hay al menos un material sobrante, Herobrine lo pone en el horno uno por uno, hasta que no haya espacio para el siguiente material o ya haya puesto todos.
#    2. El horno cocina k gramos del material que esté primero en la cola (o simplemente todo lo que quede del material).
#   Entrada
#    La primera línea de entrada contiene los enteros n, h y k (1≤n≤100000,1≤k≤h≤109) — el número de materiales, la capacidad del horno y la cantidad de gramos que este puede cocinar cada segundo, respectivamente.
#    La primera línea de entrada contiene los enteros
#    ,
#    y
#    (1≤
#    ≤100000,1≤
#    ≤
#    ≤10
#    9
#    ) — el número de materiales, la capacidad del horno y la cantidad de gramos que este puede cocinar cada segundo, respectivamente.
#    La segunda línea contiene n enteros ai (1≤ai≤h) — el peso en gramos de cada material.
#    La segunda línea contiene
#    enteros
#    ai
#    ) — el peso en gramos de cada material.
#   Salida
#    Imprime un entero, el número de segundos requeridos para cocinar todos los materiales siguiendo el proceso descrito en el enunciado del problema.
#   Ejemplo Entrada
#    5 6 35 4 3 2 1
#   Ejemplo Salida
#    5
#   Ayuda

