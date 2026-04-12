# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=6
## https://jv.umsa.bo/oj/problem.php?id=1083
#    Copiado al portapapeles
#  Truco de Magia
#  Enviar
#  Estado
#  Descripción
#    Recientemente usted fue a un espectáculo de magia. Usted estaba muy impresionado por uno de los trucos, por lo que decidió tratar de averiguar el secreto detrás de él!
#    El mago comienza disponiendo 16 tarjetas en una cuadrícula: 4 filas de tarjetas, con 4 cartas en cada fila. Cada tarjeta tiene un número diferente de 1 a 16 escrito en el lado que está mostrando. A continuación, el mago pide un voluntario para elegir una tarjeta, y para decirle qué fila que la tarjeta está en.
#    Por último, el mago arregla las 16 cartas en una cuadrícula de nuevo, posiblemente en un orden diferente. Una vez más, le pide al voluntario qué fila su tarjeta está en. Con sólo las respuestas a estas dos preguntas, el mago entonces correctamente determina qué tarjeta eligió el voluntario. Increíble, ¿no?
#    Usted decide escribir un programa para ayudarle a entender la técnica del mago. El programa le dará las dos disposiciones de las tarjetas, y las respuestas de los voluntarios a las dos preguntas: el número de fila de la tarjeta seleccionada en la primera disposición, y el número de fila de la tarjeta seleccionada en la segunda disposición. Las filas están numeradas del 1 al 4 de arriba a abajo.
#    Su programa debe determinar qué tarjeta eligió el voluntario; o si hay más de una tarjeta al voluntario podría haber elegido (el mago hizo un mal trabajo); o si no hay ninguna tarjeta en consonancia con las respuestas de los voluntarios (el voluntario engañado).
#   Entrada
#    La primera línea de la entrada da el número de casos de prueba, casos de prueba T. T siguen. Cada caso de prueba comienza con una línea que contiene un entero: la respuesta a la primera pregunta. Los próximos 4 líneas representan la primera disposición de las tarjetas: cada uno contiene 4 enteros, separados por un solo espacio. La siguiente línea contiene la respuesta a la segunda pregunta, y los siguientes cuatro líneas contiene la segunda disposición en el mismo formato.
#   Salida
#   Ejemplo Entrada
#    321 2 3 45 6 7 89 10 11 1213 14 15 1631 2 5 43 11 6 159 10 7 1213 14 8 1621 2 3 45 6 7 89 10 11 1213 14 15 1621 2 3 45 6 7 89 10 11 1213 14 15 1621 2 3 45 6 7 89 10 11 1213 14 15 1631 2 3 45 6 7 89 10 11 1213 14 15 16
#   Ejemplo Salida
#    Case #1: 7Case #2: Bad magician!Case #3: Volunteer cheated!
#   Ayuda

