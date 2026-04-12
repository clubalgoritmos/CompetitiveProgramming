# https://jv.umsa.bo/oj/problem.php?cid=2826&pid=13
## https://jv.umsa.bo/oj/problem.php?id=1690
#  PARTIDA
#  Enviar
#  Estado
#  Descripción
#    Vivimos en un futuro muy caótico, ha habido muchos avances tecnológicos y estos han hecho que distintas empresas e industrias quieran trabajar juntas y usar alta tecnología. Es el caso de la industria de los videojuegos, una empresa muy reconocida en un futuro es Saito Geimu, ellos han estado desarrollando en secreto una interfaz de realidad aumentada con algoritmos de inteligencia artificial para juegos de terror.
#    La interfaz y el algoritmo tienen una tarea sencilla, descubrir tus mayores temores y hacerte pensar que están sucediendo en la realidad.
#    Un típico mochilero estadounidense llamado Cooper, ha perdido todo su dinero y no tiene dinero para volver a su país decide ir a probar la interfaz de Saito Geimu, lo que no sabe es que esa interfaz es muy avanzada y es muy complicado librarse de ella.
#    Durante las pruebas, Cooper es introducido en una mansión, super terrorífica, en la cual la interfaz comienza a hacer lo suyo, asustarlo.
#    Como Cooper está muy asustado, te llama a ti para que lo ayudes, él te da el mapa de la mansión, como si fuera una matriz de N x M y te pide que le digas si es que existe una zona segura en la mansión en la que el pueda caminar para que la interfaz no tenga mucho efecto en él.
#    El mapa de la mansión contendrá en cada casilla de la matriz un número, al que llamaremos Entropía del Terror, esto nos indica cuanto terror tendremos si pasamos por esa parte de la mansión. Por ejemplo, el siguiente mapa puede ser un ejemplo de un mapa de la mansión.
#    N=5 M=5
#    1
#    2
#    7
#    -1
#    4
#    5
#    6
#    -7
#    8
#    3
#    10
#    -2
#    A la derecha del mapa se puede observar que, sí existen zonas seguras en este mapa, de hecho, existe más de una, ahora te estarás preguntando porque esta zona es segura, antes que nada debes entender algo, Cooper no puede quedarse parado en ninguna casilla, por lo que no puede existir una zona segura de sólo una casilla de la matriz, una zona segura debe de ser de por lo menos 2 casillas (no necesariamente contiguas). Bueno en la figura de la izquierda las zonas pintadas son seguras porque si Cooper camina por ellas siempre estará reduciendo su Entropía del Terror, por ejemplo, si camina por la zona amarilla siempre estará reduciendo su entropía del terror. Entonces una zona segura es aquella en la que podemos caminar siempre reduciendo nuestra entropía del terror. Por último, si por alguna razón, la cantidad de zonas seguras supera a la cantidad de zonas no seguras, entonces es una trampa y debes HUIR enseguida.
#   Entrada
#    La entrada contendrá un solo caso de prueba, se te darán dos enteros N y M (2<=N,M<=40), que son las dimensiones del mapa de la mansión, luego siguen N filas cada una con M números xij (-100<=xij<=100) que representan las entropías del terror en cada posición.
#   Salida
#    Debes imprimir ESTAS SEGURO, si es que existe una zona segura o HUYE RAPIDO, en caso de que no exista ninguna zona segura.
#   Ejemplo Entrada
#    5 51 2 7 -1 44 5 6 -7 85 5 -1 -1 23 7 5 10 104 4 -1 1 2
#   Ejemplo Salida
#    ESTAS SEGURO
#   Ayuda

