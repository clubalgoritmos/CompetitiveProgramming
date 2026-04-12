# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=39
## https://jv.umsa.bo/oj/problem.php?id=1195
#    Copiado al portapapeles
#  No Detectado
#  Enviar
#  Estado
#  Descripción
#    El Departamento de Defensa ha estado diseñando robots autónomos que pueden infiltrarse en las zonas de guerra y otros lugares hostiles con el fin de llevar a cabo misiones. Ahora quieren poner a prueba su último diseño, el Penetrator1700, y te han contratado para ayudar a diseñar el entorno de prueba.El entorno de prueba es un campo rectangular con algunos sensores colocados dentro del campo. Cada sensor tiene una cierto radio que define la región dentro de la cual se puede detectar un robot. ¿Tienes que diseñar el campo para tener tantos sensores como sea posible permitiendo al mismo tiempo una ruta a través del campo, que evite la detección.El campo es una región del plano de coordenadas, definido por 0 <= x <= 200 y 0 <= y <= 300. El robot puede ser modelado por un punto que debe permanecer en el campo en todo momento. Se inicia en la parte inferior del campo (y = 0) y debe terminar en la parte superior del campo (y = 300), y no debe pasar dentro del alcance de cualquier sensor. Hay N ubicaciones de los sensores dados por tres números enteros (x, y, r), donde cada (x, y) es un punto en el campo, y r es su radio de detección. Los círculos que detectan los sensores pueden solaparse, pero nunca serán tangentes entre sí ni con el límite del campo. Todos los sensores están inicialmente inactivos. Usted debe encontrar el mayor valor de K tal que si los sensores 1, 2, 3,. . . , K se activan hay un camino para el robot a través del campo, pero sin camino si el sensor (k + 1) también se activa. Se garantiza que no hay camino si todos los N sensores son activados.
#    Los círculos corresponden a los tres primeros ejemplos
#    Ejemplo 1636 228 58164 224 5888 170 4293 105 42167 85 5828 44 58Salida para el ejemplo 12Ejemplo 2636 228 5828 44 58164 224 5888 170 4293 105 42167 85 58Salida para el ejemplo 23Ejemplo 3628 44 5836 228 5888 170 4293 105 42164 224 58167 85 58Salida para el ejemplo 3Ejemplo 43100 150 10130 30 10170 30 100Salida para el ejemplo 40
#   Entrada
#    La entrada comienza con un numero positivo N <=0. Cada una de las N líneas que siguen tienen tres enteros separados por un espacio,que representan x,y,r para cada sensor, donde r <= 300. Todos los sensores están en diferentes posiciones (x,). Los tres primeros ejemplos corresponden a la figura de ejemplo.
#   Salida
#    Escriba un solo entero que (puede ser 0) dando el k más grande tal como se describió.
#   Ejemplo Entrada
#    636 228 58164 224 5888 170 4293 105 42167 85 5828 44 58
#   Ejemplo Salida
#    2
#   Ayuda

