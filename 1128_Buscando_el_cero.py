# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=18
## https://jv.umsa.bo/oj/problem.php?id=1128
#    Copiado al portapapeles
#  Buscando el cero
#  Enviar
#  Estado
#  Descripción
#    Se le dará 4 vectores de tamaño N ahora debe encontrar todas las cuadruplas que su suma sea 0.
#    Ej:
#    Vector 1
#    -9
#    5
#    6
#    2
#    3
#    1
#    Vector 2
#    -6
#    Vector 3
#    -3
#    9
#    7
#    Vector 4
#    0
#    -1
#    4
#    Como puede observar la cruadrupla $(-9,6,3,0)$ y la cuadrupla $(6,-6,1,-1)$ su suma es igual a 0 (ojo hay mas cuatruplas).
#    Ahora su trabajo es encontrar todas las cuadrulas que su suma sea igual a 0.
#   Entrada
#    La primera linea sera un entero $T$ es el numero de casos de prueba, seguido por $N$ que es el tamaño de los 4 vectores las siguientes $N$ lineas son 4 valores que son elementos de los 4 vectores respectivamente.
#   Salida
#    La salida consiste en un numero que describe todos las cuadruplas que sumen 0.
#   Ejemplo Entrada
#    16-45 22 42 -16-41 -27 56 30-36 53 -37 77-36 30 -75 -4626 -38 -10 62-32 -54 -6 45
#   Ejemplo Salida
#   Ayuda
#    El caso de entrada tiene 5 cuadruplas que su suma es igual a 0 : $(-45,-27,42,30), (26,30,-10,-46), (-32,22,56,-46), (-32,30,-75,77), (-32,-54,56,30)$.
#    Se puede hallar la solucion si probamos todas las combinaciones de forma recursiva

