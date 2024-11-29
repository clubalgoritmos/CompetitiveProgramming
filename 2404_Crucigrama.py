# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=205
## https://jv.umsa.bo/oj/problem.php?id=2404
#    Copiado al portapapeles
#  Crucigrama
#  Enviar
#  Estado
#  Descripción
#    En este crucigrama te dan una cuadrado que tiene muchas letras y un lista de palabras.Tu trabajo es encontrar cada una de las palabras en el cuadrado.El ejemplo muestra un cuadrado de 10 por 10
#    Ahora suponga que tiene que buscar las palabras: NEWTON, WILSON, UNION, LUCAS.NEWTON comienza en la posición(3,0), WILSON en la posición (4,3), UNION en la posición(8,0) y LUCAS en la posición (1,6).Lo que se pide es que encuentres donde comienza la palabra y indiques si hay que recorrer horizontalmente (h), verticalmente (v) o en diagonal de arriba hacia abajo (d). En este ejemplo el resultado es:NEWTON (3,0) -HWILSON (4,3) -DUNION (8,0) -HLUCAS (1,6) -VPara obtener la respuesta correcta primero debe verificar si la palabra existe horizontalmente, después verticalmente y finalmente en diagonal de izquierda a derecha y de arriba hacia abajo.Si existiera en más de una posición solo debe listar la primera encontrada.
#    Ahora suponga que tiene que buscar las palabras: NEWTON, WILSON, UNION, LUCAS.NEWTON comienza en la posición(3,0), WILSON en la posición (4,3), UNION en la posición(8,0) y LUCAS en la posición (1,6).
#    Lo que se pide es que encuentres donde comienza la palabra y indiques si hay que recorrer horizontalmente (h), verticalmente (v) o en diagonal de arriba hacia abajo (d). En este ejemplo el resultado es:NEWTON (3,0) -HWILSON (4,3) -DUNION (8,0) -HLUCAS (1,6) -VPara obtener la respuesta correcta primero debe verificar si la palabra existe horizontalmente, después verticalmente y finalmente en diagonal de izquierda a derecha y de arriba hacia abajo.Si existiera en más de una posición solo debe listar la primera encontrada.
#   Entrada
#    La entrada consiste de un caso de prueba. Las primeras 50 lineas cada una de 50 caracteres corresponden al crucigrama. Luego vienen las palabras a buscar, que terminan cuando es fin de archivo.
#    Para verificar si es el ejemplo, cuente el número de caracteres de la primera línea. Si es 10 corresponde al ejemplo.
#   Salida
#    En la salida escriba las palabras, su posición y si están en posición Horizontal, Vertical, o Diagonal como se muestra en el ejemplo.
#   Ejemplo Entrada
#    XNDDPYJAQLWQLUZVLZHRZIIZWXUUCXNEWTONCDTPEOQWLAATTBTCPIISSMZLJTGUELRQCZJBRSTLSCJNUNIONWLOQHSMJSFXHQNNNEWTONWILSONUNIONLUCAS
#   Ejemplo Salida
#    NEWTON (3, 0) -HWILSON (4, 3) -DUNION (8, 0) -HLUCAS (1, 6) -V
#   Ayuda

