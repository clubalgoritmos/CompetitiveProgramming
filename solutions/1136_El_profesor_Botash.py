# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=22
## https://jv.umsa.bo/oj/problem.php?id=1136
#    Copiado al portapapeles
#  El profesor Botash
#  Enviar
#  Estado
#  Descripción
#    El profesor Botash (luego de haber sido un pésimo entrenador pokemon Botash decidió dedicarse al estudio de los Pokemon) tiene muchos Pokemon en su laboratorio. El tiene ahora un número casi infinito de Charmander, Bulbasaur y Squirtle y el no quiere darlos gratis a los nuevos entrenadores Pokemon así que los venderá.
#    Ahora imagina que son N niños esperando tener su primer pokemon. Oak los pone en fila. El decidio que dos niños que sean vecinos no pueden tener el mismo pokemon. Los vecinos de un niño i son el niño i-1 y el i+1. El primero y el último obviamente solo tienen un vecino. Un niño puede tener 1 de los 3 pokemon (sin infringir la anterior condición) y pagar para obtenerlo. El costo de un cierto pokemon no es el mismo para todos los niños. El costo de un cierto pokemon para el niño i es asignado al azar.
#    Por ejemplo el costo de un Charmander, Bulbasaur y un Squirtle para un niño son 1, 100, 100 respectivamente, y para otro podrían ser 100,1,100. Los niños están enojados con Botash por venderles los pokemon, cuando Oak los regalaba así que ellos piensan darle una lección comprando los pokemon óptimamente para que Botash gané lo mínimo posible.
#    Entonces dado el número de niños y el costo de comprar los 3 pokemon para cada niño halla la cantidad mínima de dinero que Botash podrá ganar. Recuerda dos niños vecinos no pueden compartir el mismo pokemon.
#   Entrada
#    Linea 1: Número de casos de prueba. (T<=10)
#    Linea 2: El número de niños N (N<=10⁵)
#    Las siguientes líneas tienen el precio de comprar a Charmander, Bulbasaur y Squirtle (en ese orden).
#   Salida
#    El costo mínimo de comprar los pokemon.
#   Ejemplo Entrada
#    231 100 100100 1 100100 100 131 100 100100 100 1001 100 100
#   Ejemplo Salida
#    3102
#   Ayuda
#    Probar todos los casos en los que se puede comprar un pokemon y memoizar

