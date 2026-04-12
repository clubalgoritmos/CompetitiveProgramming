# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=58
## https://jv.umsa.bo/oj/problem.php?id=1343
#    Copiado al portapapeles
#  Patrones de Fibonacci
#  Enviar
#  Estado
#  Descripción
#    Veamos el último dígito de cada número de Fibonacci. \[ 0 , 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, ... \]La pregunta que nos hacemos es si hay un patrón para estos dígitos\[ 0 , 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, ... \]La respuesta es si, después de $60$ números de vuelven a repetir, en forma cíclica.En un caso más general podemos hallar cada uno de los números módulo $2,3,4..$.Por ejemplo si hallamos los valores después de hallar al módulo $2$ vemos que los restos son $0, 1, 1, 0, 1, 1, 0$. La respuesta es que cada 3 números se vuelve a repetir la serie.
#   Entrada
#    La entrada consiste de varias líneas. En cada línea hay un número $1 \leq a \leq 10000$ que utilizaremos para hallar el módulo. La entrada termina cuando no hay más datos.
#   Salida
#    Por cada línea de entrada en la salida se imprimirá un número entero que indica cada cuantos números se repite la secuencia resultante de hallar el módulo $a$ sobre los números de Fibonacci.
#   Ejemplo Entrada
#    2345101000
#   Ejemplo Salida
#    38620601500
#   Ayuda

