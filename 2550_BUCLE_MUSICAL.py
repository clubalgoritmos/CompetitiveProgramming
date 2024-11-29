# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=218
## https://jv.umsa.bo/oj/problem.php?id=2550
#    Copiado al portapapeles
#  BUCLE MUSICAL
#  Enviar
#  Estado
#  Descripción
#    Un bucle musical es una pequeña sección de música compuesta para reproducirse continuamente (es decir, la sección sese vuelve a reproducir cuando llega al final), de forma fluida. Los bucles se utilizan en muchos estilos de popularesmúsica (hip hop, techno, etc), así como en juegos de computadora, especialmente juegos casuales en Internet.Los bucles se pueden digitalizar, por ejemplo, utilizando PCM (Modulación de código de pulso), una técnica para representar señales analógicas que se usa ampliamente en audio digital. En PCM, la magnitud de la señal esmuestreados a intervalos regulares, y los valores muestreados se almacenan en secuencia. Para producir el sonido delos datos muestreados, el procedimiento se aplica a la inversa (demodulación).Pancracio trabaja para una casa de software de juegos y compuso un hermoso bucle musical, codificado en PCM.Al analizar la forma de onda de su bucle en el software de edición de audio, Pancracio sintió curiosidad cuandonotó el número de "picos". Un pico en una forma de onda es el valor de una muestra que representa unmáximo o mínimo. La siguiente figura ilustra (a) una forma de onda y (b) el bucle formado con estaforma de onda, que contiene 48 picos.A) Forma de onda B) Forma de onda en buclePancracio es un querido amigo tuyo. El ha pedido tu ayuda para determinar cuántos picos existen en su bucle musical.
#   Entrada
#    La entrada contiene varios casos de prueba. La primera línea de un caso de prueba contiene un número entero N, que representael número de muestras en el bucle musical compuesto por Fernanda (2 <= N <= 104). La segundala línea contiene N enteros , separados por espacios, que representan la secuencia de magnitudes muestreadas(−104 <= hola <= 104)para 1 <= i <= N, H1 ̸= HN y Hi ̸= Hi+1 para 1 <= i <= N). Observe que H1 sigueHN cuando se reproduce el bucle.El final de la entrada se indica mediante una línea que contiene solo un cero.
#   Salida
#    Para cada caso de prueba en la entrada, su programa debe imprimir una sola línea, que contenga un número entero, el númerode picos que existen en el bucle musical.
#   Ejemplo Entrada
#    32 7 9118 10 22 -15 9 7 25 -30 4 5 -7043 2 -7 60
#   Ejemplo Salida
#    282
#   Ayuda

