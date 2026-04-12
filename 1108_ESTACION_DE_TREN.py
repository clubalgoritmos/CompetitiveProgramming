# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=13
## https://jv.umsa.bo/oj/problem.php?id=1108
#    Copiado al portapapeles
#  ESTACION DE TREN
#  Enviar
#  Estado
#  Descripción
#    En una fría noche de invierno nuestro héroe Vasya estaba en una cola de tren para comprar un boleto para final del campeonato de programación. Como suele ocurrir, el cajero dijo que iba a estar fuera durante 5 minutos y se dejó durante una hora. Entonces Vasya, no aburrirse, comenzó a analizar un mecanismo como una cola. Los resultados asombraron a Vasya.
#    Cada hombre se caracteriza por dos números:  ,que es la importancia de su tarea actual (el mayor es el número, más importante es la tarea) y el número de CI, que es una imagen de su conciencia. Números   formar la permutación de los números de 1 a n.
#    Deje que la cola consiste en n - 1 personas en el momento. Echemos un vistazo a la forma en que la persona que vino número n se comporta. En primer lugar, se encuentra al final de la cola y el hace lo siguiente: si la importancia de la tarea   del hombre frente a él es menos de una, intercambian sus lugares (se parece a esto: el hombre número n pide al uno delante de él: "Ehh ... Discúlpeme por favor, pero es muy importante para mí ... ¿podrías por favor hágamelo muevo la cola?"), entonces de nuevo plantea la pregunta al hombre delante de él y así sucesivamente . Pero en caso de que   es mayor que una, moviendo la cola se detiene. Sin embargo, el hombre número n puede realizar la operación no más veces  .
#    En nuestra tarea supongamos que por el momento en que el hombre número n se une a la cola, el proceso de swaps entre n - 1 se han detenido. Si el intercambio es posible que se lleva a cabo necesariamente.
#    Su tarea es ayudar modelo Vasya el proceso descrito y encontrar el orden en que las personas van a estar en cola cuando todos los swaps se detienen.
#   Entrada
#    La primera línea de entrada contiene un entero n, que es el número de personas que se ha unido a la cola (1 ≤ n ≤ 105). En las siguientes n líneas se dan descripciones de las personas con el fin de su venida - enteros separados por espacios   y  (1 ≤ ai ≤ n, 0 ≤   ≤ n). Cada descripción se encuentra en s de una sola línea. De Todos los  son diferentes.
#   Salida
#    Salida de la permutación de los números de 1 a n, que significa la cola formada de acuerdo con las reglas descritas anteriormente, comenzando desde el principio hasta el final. En esta sucesión el número de orden i representa el número de una persona que va a hacer cola en el número de sitio en el que después de los extremos de swaps. La gente se numera comenzando con 1 en el orden en que se daban en la entrada. Separe los números por un espacio.
#   Ejemplo Entrada
#    21 02 131 32 33 352 31 44 33 15 2
#   Ejemplo Salida
#    2 13 2 13 1 5 4 2
#   Ayuda
#    Simular el proceso con las codiciones dadas en el problema.

