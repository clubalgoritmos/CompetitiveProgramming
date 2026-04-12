# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=173
## https://jv.umsa.bo/oj/problem.php?id=2104
#    Copiado al portapapeles
#  Tetris
#  Enviar
#  Estado
#  Descripción
#    Se le proporciona un campo de Tetris que consta de $n$ columnas. La altura inicial de la $i$-ésima columna del campo es $a_{i}$ bloques. En la parte superior de estas columnas puede colocar solo figuras de tamaño $2 × 1$ (es decir, la altura de esta figura es de $2$ bloques y el ancho de esta figura es de $1$ bloque). Tenga en cuenta que no puede rotar estas figuras.
#    Su tarea es decir si puede despejar todo el campo colocando tales figuras.
#    De manera más formal, el problema se puede describir así:
#    El siguiente proceso ocurre cuando al menos un $a_{i}$ es mayor que $0$:
#    Coloca una figura $2 × 1$ (elija alguna $i$ de $1$ a $n$ y reemplace $a_{i}$ con $a_{i} + 2$);
#    luego, mientras que todas las $a_{i}$ son mayores que cero, reemplace cada $a_{i}$ con $a_{i} − 1$.
#    Y su tarea es determinar si es posible limpiar todo el campo (es decir, finalizar el proceso descrito), eligiendo correctamente los lugares para las nuevas figuras.
#    Tienes que responder $t$ casos de prueba independientes.
#   Entrada
#    La primera línea de la entrada contiene un número entero $t$ ($1 \leq t \leq 100$): el número de casos de prueba.
#    Las siguientes $2t$ líneas describen casos de prueba. La primera línea del caso de prueba contiene un número entero $n$ ($1 \leq n \leq 100$): el número de columnas en el campo Tetris. La segunda línea del caso de prueba contiene $n$ números enteros(Index 1) $a_{1}$, $a_{2}$,…, $a_{n}$ ($1 \leq a_{i} \leq 100$), donde $a_{i}$ es la altura inicial de la $i$-ésima columna del campo Tetris.
#   Salida
#    Para cada caso de prueba, imprima la respuesta: "YES" (sin comillas) si puede borrar todo el campo de Tetris y "NO"(sin comillas) en caso contrario.
#   Ejemplo Entrada
#    431 1 341 1 2 1211 111100
#   Ejemplo Salida
#    YESNOYESYES
#   Ayuda
#    El primer caso de prueba del campo de ejemplo se muestra a continuación:
#    Las líneas grises son límites del campo de Tetris. Tenga en cuenta que el campo no tiene límite superior.
#    Una de las respuestas correctas es colocar primero la figura en la primera columna. Luego, después del segundo paso del proceso, el campo se convierte en [2,0,2]. Luego coloque la figura en la segunda columna y después del segundo paso del proceso, el campo se convierte en [0,0,0].
#    Y el segundo caso de prueba del campo de ejemplo se muestra a continuación:
#    Se puede demostrar que no puede hacer nada para finalizar el proceso.
#    En el tercer caso de prueba del ejemplo, primero coloca la figura en la segunda columna después del segundo paso del proceso, el campo se convierte en [0,2]. Luego coloque la figura en la primera columna y después del segundo paso del proceso, el campo se convierte en [0,0].
#    En el cuarto caso de prueba del ejemplo, coloque la figura en la primera columna, luego el campo se convierte en [102] después del primer paso del proceso, y luego el campo se convierte en [0] después del segundo paso del proceso.

