# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=77
## https://jv.umsa.bo/oj/problem.php?id=1398
#    Copiado al portapapeles
#  Suma Ascii
#  Enviar
#  Estado
#  Descripción
#    Hoy en día existen aplicaciones para teléfonos inteligentes que pueden traducir texto e inclusive resolver problemas de matemáticas con solo enfocar la cámara del celular a ellos. Su trabajo es implementar una funcionalidad más simple que es una reminiscencia del pasado reciente. Sume dos numero enteros representados como una arte ASCII.Un arte ASCII es una matriz de caracteres que tienen exactamente 7 filas de altura con cada carácter individual representado por un punto y una letra x.Una expresión de la forma $a+b$ se muestra en el ejemplo. Ambos números son enteros positivos. La expresión se convierte en un arte ASCII como matrices de $7x5$ que se concatenan una alado de la otra, incluyendo el signo de sumar.Las matrices siguientes muestran todos los números incluyendo el signo de suma.xxxxx ....x xxxxx xxxxx x...x xxxxx xxxxx xxxxx xxxxx xxxxx .....x...x ....x ....x ....x x...x x.... x.... ....x x...x x...x ..x..x...x ....x ....x ....x x...x x.... x.... ....x x...x x...x ..x..x...x ....x xxxxx xxxxx xxxxx xxxxx xxxxx ....x xxxxx xxxxx xxxxxx...x ....x x.... ....x ....x ....x x...x ....x x...x ....x ..x..x...x ....x x.... ....x ....x ....x x...x ....x x...x ....x ..x..xxxxx ....x xxxxx xxxxx ....x xxxxx xxxxx ....x xxxxx xxxxx .....Dado un arte ASCII para una expresión $a+b$, encuentre el resultado de la suma y escríbalo en forma de arte ASCII.
#    xxxxx ....x xxxxx xxxxx x...x xxxxx xxxxx xxxxx xxxxx xxxxx .....x...x ....x ....x ....x x...x x.... x.... ....x x...x x...x ..x..x...x ....x ....x ....x x...x x.... x.... ....x x...x x...x ..x..x...x ....x xxxxx xxxxx xxxxx xxxxx xxxxx ....x xxxxx xxxxx xxxxxx...x ....x x.... ....x ....x ....x x...x ....x x...x ....x ..x..x...x ....x x.... ....x ....x ....x x...x ....x x...x ....x ..x..xxxxx ....x xxxxx xxxxx ....x xxxxx xxxxx ....x xxxxx xxxxx .....
#   Entrada
#    La entrada consiste exactamente de 7 lineas que contiene el arte ASCII para la expresión de la forma $a+b$, donde ambos son números positivos. Cada uno con un máximo de nueve dígitos sin ceros a la izquierda.
#   Salida
#    Por cada caso de prueba escriba 7 linea con el arte ASCII correspondiente al resultado de la suma sin ceros a la izquierda.
#   Ejemplo Entrada
#    ....x.xxxxx.xxxxx.x...x.xxxxx.xxxxx.xxxxx.......xxxxx.xxxxx.xxxxx....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x....x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.....x.xxxxx.xxxxx.xxxxx.x...x....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x....x.xxxxx.xxxxx.....x.xxxxx.xxxxx.....x.......xxxxx.xxxxx.xxxxx
#   Ejemplo Salida
#    ....x.xxxxx.xxxxx.xxxxx.x...x.xxxxx.xxxxx....x.....x.....x.x.....x...x.x.........x....x.....x.....x.x.....x...x.x.........x....x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.....x....x.x.........x.....x.....x.....x.....x....x.x.........x.....x.....x.....x.....x....x.xxxxx.xxxxx.xxxxx.....x.xxxxx.....x
#   Ayuda

