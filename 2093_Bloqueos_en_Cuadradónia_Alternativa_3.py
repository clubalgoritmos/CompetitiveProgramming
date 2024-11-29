# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=172
## https://jv.umsa.bo/oj/problem.php?id=2093
#    Copiado al portapapeles
#  Bloqueos en Cuadradónia Alternativa 3
#  Enviar
#  Estado
#  Descripción
#    Calles horizontales
#    Calles Verticales
#    Cuadradónia es una ciudad bien organizada. Recibe su nombre debido a la forma cuadrada que tiene vista desde el aire, y debido a su cuadrado sistema de calles. Entre sus habitantes, hay quienes ya se cansaron de que todo esté tan rectilíneo, y son estas mismas personas las que han comenzado a bloquear las esquinas de las calles, por un futuro más redondo.El sistema de calles presente en
#    Cuadradónia
#    es una ciudad bien organizada. Recibe su nombre debido a la forma cuadrada que tiene vista desde el aire, y debido a su cuadrado sistema de calles. Entre sus habitantes, hay quienes ya se cansaron de que todo esté tan rectilíneo, y son estas mismas personas las que han comenzado a bloquear las esquinas de las calles, por un futuro más redondo.
#    es único. Existen exactamente
#    $N$
#    calles horizontales y
#    calles verticales que al
#    intersectarse
#    entre sí resultan en (
#    $N * N$
#    ) esquinas. Toda calle horizontal pasa por las demás calles verticales, y toda calle vertical por las demás calles horizontales. En la ciudad, cada calle recibe un número especial que la identifica:
#    Las calles horizontales han sido numeradas desde
#    $0$
#    hasta
#    $N-1$
#    , de arriba hacia abajo.
#    Las calles verticales han sido numeradas desde
#    , de derecha a izquierda.
#    Para referirse a una esquina, la gente menciona primero el número de la calle horizontal y luego el número de la calle vertical. Por ejemplo, el cruce de la horizontal 5 con la vertical 8 se escribiría simplemente
#    $(5, 8)$
#    .
#    Debido a los bloqueos, desplazarse por la ciudad ya no es tan simple, y el presidente de la Organización de Ciudadanos Ejemplares, Prudentes y Bondadosos (
#    OCEPB
#    ) lo sabe. Él debe trasladarse desde su casa en la esquina
#    $(X_o, Y_o)$
#    hasta la sede de la
#    en la esquina
#    $(X_f, Y_f)$
#    , donde se reunirá con un representante de la Organización de Buenos Individuos (
#    OBI
#    ).
#    Los bloqueadores no son tontos se han dado cuenta que la
#    ha contratado un programador para calcular la ruta mas corta y saben que tomarán ese camino. Una vez que salen con destino a la reunión calculan la ruta más corta y ponen un bloqueo en la llegada.
#    Para decidir si te va ha ser bloqueado te han pedido que escribas un programa que indique si hay una ruta alternativa. No debes dar la ruta, solo debe indicar si va a ser bloqueado al llegar a su destino o es posible llegar.
#   Entrada
#    La entrada consiste de varios casos de prueba, donde cada caso de prueba tiene varias líneas. A continuación se describe el formato de cada caso:
#    En la primera línea se encuentra un único entero
#    (
#    $1 \leq N \leq 20$
#    ) que indica el número de calles verticales y horizontales.
#    -
#    En la segunda línea se encuentran cuatros enteros
#    $X_o$
#    ,
#    $Y_o$
#    $X_f$
#    $Y_f$
#    que denotan la esquina de origen
#    y la esquina de destino
#    $(Xf, Yf)$
#    . Se garantiza que las esquinas dadas son válidas y que la esquina de origen no es la misma que la de destino.
#    A continuación siguen
#    líneas con
#    caracteres cada una, indicando la presencia/ausencia de bloqueos en cada esquina de la ciudad. Un carácter
#    B
#    indica que la esquina está bloqueada y un carácter L
#    que una esquina está libre.
#    La entrada termina cuando
#    es 0. Este caso no debe ser procesado.
#   Salida
#    Por cada caso de prueba: En caso de que exista una ruta sin bloqueos desde el origen al destino, debes imprimir
#    HAY RUTA POSIBLE. Si fuese imposible llegar o si la esquina de destino/origen está bloqueada, imprime
#    NO HAY RUTA POSIBLE. Si va a ser bloqueado al llegar escriba
#    HAY RUTA POSIBLE PERO SERA BLOQUEADO
#   Ejemplo Entrada
#    50 1 1 4BLBLBLLLLLBBLLLLBLBBBBLLB50 1 1 4BLBLBLLLLLBBBLBLBLBBBBLLB0
#   Ejemplo Salida
#    HAY RUTA POSIBLEHAY RUTA POSIBLE PERO SERA BLOQUEADO
#   Ayuda

