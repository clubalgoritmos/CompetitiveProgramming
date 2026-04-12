# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=235
## https://jv.umsa.bo/oj/problem.php?id=2672
#    Copiado al portapapeles
#  Secuencia de Divisores
#  Enviar
#  Estado
#  Descripción
#    Para este problema se van ha hallar la suma de los divisores propios de un número excluyendo al mismo, por ejemplo, los divisores de n=10 son 5+2+1=8.
#    Este proceso repite la suma de los divisores de $n$ hasta que no hayan más divisores en la suma. Vea el caso n=10:
#    1. suma de los divisores de 10: 5 + 2 + 1 = 8.   2. suma de los divisores de 8: 4 + 2 + 1 = 7.   3. suma de los divisores de 7: 1   4. suma de los divisores de 1: 0
#    Vea que en muchos casos no es posible llegar a cero. Por ejemplo con n=6, se tiene la suma de sus divisores 3+2+1=6, que produce un ciclo infinito. Pondremos nombres a los números que pueden aparecer en este proceso.
#    - Números corrientes, los que al realizar el ciclo descrito llegan a cero.
#    - Número perfecto cuando la suma de sus divisores da el mismo número, como el ejemplo la suma de divisores de 6 es: 3+2+1=6.
#    - Si la cantidad de ciclos supera $10^3$ se llamaran números indefinidos.
#    - Si la suma de sus divisores da un número después de la segunda iteración vuelve al numero original los denominaremos números románticos. Por ejemplo: la suma de factores de 220 es 287 y de 287 es 220. Vea que en este proceso solo intervienen dos números.
#    - Cuando la suma de los divisores es mayor al número se llaman \textbf{abundantes}. Por ejemplo los factores de 12 suman: 6+4+3+2+1=16.- Consideremos el 95, la suma de sus factores es: 1+5+19=25, luego la suma de factores de 25 es 1+5=6 y 6 se repite. Estos números los denominaremos inspiradores.
#    - Los números amigables se define cuando en algún momento del ciclo se repite alguna suma de divisores y no es número romántico.
#   Entrada
#    La entrada consiste de múltiples casos de prueba. La primera línea tiene el número de casos de prueba. Por cada caso de prueba viene una lista de números en una línea.
#   Salida
#    Por cada caso de prueba imprima en una línea el tipo de núymero como se explico.Primero en el resultado de salida se coloca el número que se esta probando, luego la palabra \textit{abundante} si corresponde y a continuación la clasificación que le corresponde.
#   Ejemplo Entrada
#    17 24 28 220 95 276 2856 2
#   Ejemplo Salida
#    7 corriente24 abundante corriente28 perfecto220 abundante romántico95 inspirador276 abundante indefinido2856 abundante amigable2 corriente
#   Ayuda

