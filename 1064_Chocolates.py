# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=3
## https://jv.umsa.bo/oj/problem.php?id=1064
#    Copiado al portapapeles
#  Chocolates
#  Enviar
#  Estado
#  Descripción
#    Reus es el dueño de una cadena de hoteles por todo el mundo, por esta razón esta en constante movimiento entre todos sus hoteles.
#    El tiene su hotel preferido llamado MR, y siempre que regresa de algun viaje trae consigo muchos chocolates para compartirlos con sus empleados, el hotel tiene $N$ pisos y en cada piso hay una cantidad de empleados.
#    Visita cada piso comenzando del primero hasta el ultimo. El proceso para repartir los chocolates es el siguiente, cuando se encuentra el el i-esimo piso reparte la maxima cantidad de chocolates posibles de forma que cada empleado de ese piso tenga la misma cantidad de chocolates que cualquier otro empleado de ese mismo piso y luego pasa al piso siguiente asi sucesivamente hasta completar todos los pisos de su edificio favorito.
#    Una vez terminado de visitar los $N$ pisos Reus se come los chocolates que le sobraron.
#    Reus tiene miedo de excederse con el consumo de los chocolates por lo que necesita saber cuantos chocolates ha consumido al retorno de cada viaje. Pero el no recuerda la cantidad sobrante de los chocolates, pero si sabe cuantos chocolates trajo de cada viaje y también la cantidad de empleados que tiene por cada piso en su edificio.
#    Con esa información tu puedes ayudar a Reus a saber la cantidad exacta de chocolates que se comió al retornar de cada viaje.
#   Entrada
#    La primera linea de entrada contiene dos numeros enteros $N$ y $M$ $(1 \leq N, M \leq 10^5)$, que representan la cantidad de pisos del hotel y la cantidad de viajes realizados por Reus.
#    La siguiente linea contiene $N$ elementos $P_i$ $(1 \leq P_i \leq 10^{9})$ que representan a la cantidad de empleados en cada piso del hotel.
#    La siguiente linea contiene $M$ elementos $V_i$ $(1 \leq V_i \leq 10^{9})$ que representan a la cantidad de de chocolates que trajo en el i-esimo viaje.
#   Salida
#    Mostrar la cantidad de chocolates que se comio Reus por cada viaje.
#   Ejemplo Entrada
#    3 390 42 5140 79 5
#   Ejemplo Salida
#    320
#   Ayuda

