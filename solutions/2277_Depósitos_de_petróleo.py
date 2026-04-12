# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=188
## https://jv.umsa.bo/oj/problem.php?id=2277
#    Copiado al portapapeles
#  Depósitos de petróleo
#  Enviar
#  Estado
#  Descripción
#    La empresa de Yacimientos Petrolíferos Fiscales Bolivianos (YPFB) es responsable de detectar depósitos de petróleo subterráneos en distintos puntos del pais.YPFB trabaja con una gran región rectangular de terreno a la vez y crea una cuadrícula que divide el terreno en numerosas parcelas cuadradas. Luego analiza cada parcela por separado, utilizando equipos de detección para determinar si la parcela contiene petróleo o no.
#    Una parcela que contiene petroleo se llama depósito. Si dos depósitos son adyacentes, entonces son parte del mismo depósito de petróleo. Los depósitos de petroleo pueden ser bastante grandes y contener numerosos depósitos. Tu trabajo es determinar cuántos depósitos de petróleo diferentes hay en un terreno cuadriculado.
#   Entrada
#    La entrada contiene una o más cuadrículas. Cada cuadrícula comienza con una línea que contiene dos números $m$ y $n$, el número de filas y columnas en la cuadrícula, separadas por un solo espacio. Si $m = 0$ señala el final de la entrada; de lo contrario, $1 \leq m \leq 100$ y $1 \leq n \leq 100$. A continuación se encuentran $m$ líneas de $n$ caracteres cada una. Cada carácter corresponde a una parcela y es "$*$", que representa la ausencia de petroleo, o "$@$", que representa un depósito de petroleo.
#   Salida
#    Para cada cuadrícula, genere el número de depósitos de petróleo distintos. Dos depósitos diferentes forman parte del mismo depósito de petróleo si son adyacentes horizontal, vertical o diagonalmente. Un depósito de petroleo no contendrá más de $100$ parcelas.
#   Ejemplo Entrada
#    1 1*3 5*@*@***@***@*@*1 8@@****@*5 5****@*@@*@*@**@@@@*@@@**@0 0
#   Ejemplo Salida
#    0122
#   Ayuda

