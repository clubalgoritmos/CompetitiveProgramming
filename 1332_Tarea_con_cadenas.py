# https://jv.umsa.bo/oj/problem.php?id=1332
#  Tarea con cadenas
#  Enviar
#  Estado
#  Descripción
#    Pedro esta aprendiendo a programar. En su primera lección le pidieron como tarea que escriba un programa. El programa pide lo siguiente:Dada una cadena de solo letras mayusculas y minusculas:
#    Eliminar todas las vocales
#    Insertar el caracter '.' (punto) antes de cada consonante
#    Remplazar todas las consonantes mayusculas con su correspondiente en minuscula.
#    Para este problema tomaremos como vocales a las siguientes letras "A", "E", "I", "O", "U", "Y" y el resto de letras seran consonantes.La entrada del programa sera una cadena. El programa deberia mostrar solo una cadena, que sera el resultado de realizar las operaciones descritas en la cadena de entrada.
#   Entrada
#    Una sola cadena, esta cadena consiste solo de letras mayusculas y minusculas y su longitud estara entre 1 y 100 caracteres.
#   Salida
#    Imprime una cadena, que es el resultado de aplicar las operaciones descritas en la cadena de entrada.
#   Ejemplo Entrada
#    aBAcAba
#   Ejemplo Salida
#    .b.c.b
#   Ayuda
#    analize caracter por caracter realizando los pasos a travez de funciones

print("".join(["."+Si for Si in input().lower() if not Si in {"a", "e", "i", "o", "u", "y"}]))
