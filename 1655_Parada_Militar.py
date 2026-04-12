# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=115
## https://jv.umsa.bo/oj/problem.php?id=1655
#    Copiado al portapapeles
#  Parada Militar
#  Enviar
#  Estado
#  Descripción
#    En honor al día de la independencia de la nación de los Bytes el gobierno ha decidido organizar una parada militar. La guardia de honor ha recibido la orden de preparar una categoría solemne de soldados. El jefe de la guardia ha confiado esta importante misión al capitán Kilobyte, que sirve hace muchos años muy honorablemente en la guardia.El capitón sabe que hay N soldados en la guardia, y la altura del i-íesimo ($1 \leq i \leq N$) soldado es $H_i$ nanómetros. Llamamos a una secuencia de números enteros $A_i (1 \leq A_i \leq N)$ un rango. Se define un rango como solemne si la diferencia entre dos alturas de dos soldados adyacentes es menor o igual $K$ nanómetros. Eso significa que para el $A_i$ secuencia de longitud $M$ tendríamos $\| H_{A_i} - H_{A_{i+1}} 1 \| \leq K$ para todo $i, (1 \leq i \leq M - 1)$.El capitán cree que la promoción exitosa depende directamente de la longitud de la fila solemne que pudiera preparar. Su tarea es ayudar al capitán Kilobyte cumplir la orden y preparar un rango solemne con la longitud máxima posible.La siguiente imagen ilustra muestra un ejemplo:
#   Entrada
#    La primera linea de un caso de prueba contiene dos números naturales $N  (2 \leq N \leq 10^5)$ y $K (0 \leq K \leq 10^9)$ separados por un  espacio.La segunda linea del caso de prueba contiene $N$ enteros  $H_i (1 \leq H_i \leq 10^9)$ que representa la altura del i-esimo  soldado. Los números están separados por un espacio. Los soldados están  numerados secuencialmente en el orden que aparecen comenzando con 1.
#   Salida
#    La primera linea debe contener in solo numero $M$ del máximo rango solemne posible.La  segunda linea dela salida debe contener $M$ números enteros $A_i$,  separados por un espacio. Los soldados están numerados secuencialmente  en el orden que aparecen en el caso de prueba. En caso de que existan  múltiples soluciones puede imprimir cualquiera de ellas.
#   Ejemplo Entrada
#    3 201830 1800 17005 77 20 16 29 158 140170601 300200500 10 170999
#   Ejemplo Salida
#    1233 5 243 1 4 7
#   Ayuda

