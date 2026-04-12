# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=41
## https://jv.umsa.bo/oj/problem.php?id=1198
#    Copiado al portapapeles
#  Hielo2
#  Enviar
#  Estado
#  Descripción
#    Usted juega un juego de ordenador. Tu personaje se encuentra en algún nivel de una cueva de hielo de varios niveles. Con el fin de avanzar hacia adelante, tiene que descender un nivel más bajo y la única manera de hacer esto es a caer a través del hielo.
#    El nivel de la cueva en la que estas es una cuadrícula rectangular de n filas y m columnas. Cada célula consiste ya sea hielo intacto o de hielo agrietado. De cada celda se puede mover a las células que se encuentran con los suyos adyacente lado (debido a algunas limitaciones del motor de juego que no puedes hacer saltos en el mismo lugar, es decir, salto de una célula a sí mismo). Si usted se muda a la celda con hielo picado, entonces tu personaje cae a través de él y si se mueve a la celda con hielo intacto, entonces el hielo en esta celda se agrieta.
#    El nivel de la cueva en la que estas es una cuadrícula rectangular de
#    n
#    filas y
#    m
#    columnas. Cada célula consiste ya sea hielo intacto o de hielo agrietado. De cada celda se puede mover a las células que se encuentran con los suyos adyacente lado (debido a algunas limitaciones del motor de juego que no puedes hacer saltos en el mismo lugar, es decir, salto de una célula a sí mismo). Si usted se muda a la celda con hielo picado, entonces tu personaje cae a través de él y si se mueve a la celda con hielo intacto, entonces el hielo en esta celda se agrieta.
#    Vamos número de las filas con números enteros de 1 a n , de arriba a abajo y las columnas con números enteros de 1 a m de izquierda a derecha. Vamos a denotar una celda en la intersección de la r -ésima fila y la c -ésima columna como ( r , c ) .
#    Vamos número de las filas con números enteros de
#    1
#    a
#    , de arriba a abajo y las columnas con números enteros de
#    de izquierda a derecha. Vamos a denotar una celda en la intersección de la
#    r
#    -ésima fila y la
#    c
#    -ésima columna como
#    (
#    ,
#    )
#    .
#    Te vas a quedar en la celda ( r 1 , c 1 ) y esta célula está agrietada, ya que sólo ha caído aquí desde un nivel superior. Usted necesita ir a la celda ( r 2 , c 2 ) desde la salida al siguiente nivel está ahí. Puedes hacer esto?
#    Te vas a quedar en la celda
#    y esta célula está agrietada, ya que sólo ha caído aquí desde un nivel superior. Usted necesita ir a la celda
#    2
#    desde la salida al siguiente nivel está ahí. Puedes hacer esto?
#   Entrada
#    La primera línea contiene dos enteros, n y m ( 1 ≤ n , m ≤ 500 ) - el número de filas y columnas en la descripción de la cueva.
#    La primera línea contiene dos enteros,
#    y
#    1 ≤
#    ≤ 500
#    ) - el número de filas y columnas en la descripción de la cueva.
#    Cada uno de los siguientes n líneas describen el estado inicial del nivel de la cueva, cada línea se compone de m personajes " . " (Es decir, el hielo intacto) y " X "(hielo picado).
#    Cada uno de los siguientes
#    líneas describen el estado inicial del nivel de la cueva, cada línea se compone de
#    personajes "
#    " (Es decir, el hielo intacto) y "
#    X
#    "(hielo picado).
#    La siguiente línea contiene dos enteros, r 1 y c 1 ( 1 ≤ r 1 ≤ n , 1 ≤ c 1 ≤ m ) - sus coordenadas iniciales. Se garantiza que la descripción de la cueva contiene caracteres ' X 'en la celda ( r 1 , c 1 ) , es decir, el hielo en la celda de partida está agrietado inicialmente.
#    La siguiente línea contiene dos enteros,
#    ≤
#    , 1 ≤
#    ) - sus coordenadas iniciales. Se garantiza que la descripción de la cueva contiene caracteres '
#    'en la celda
#    , es decir, el hielo en la celda de partida está agrietado inicialmente.
#    La siguiente línea contiene dos enteros r 2 y c 2 ( 1 ≤ r 2 ≤ n , 1 ≤ c 2 ≤ m ) - las coordenadas de la celda a través del cual usted necesita a caer. El final de células puede coincidir con el de iniciar uno.
#    La siguiente línea contiene dos enteros
#    ) - las coordenadas de la celda a través del cual usted necesita a caer. El final de células puede coincidir con el de iniciar uno.
#   Salida
#    Si se puede llegar al destino, imprimir ' SI ', de lo contrario imprimir ' NO '.
#    Si se puede llegar al destino, imprimir '
#    SI
#    ', de lo contrario imprimir '
#    NO
#    '.
#   Ejemplo Entrada
#    4 6X...XX...XX..X..X.......1 62 2
#   Ejemplo Salida
#   Ayuda

