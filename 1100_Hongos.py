# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=9
## https://jv.umsa.bo/oj/problem.php?id=1100
#    Copiado al portapapeles
#  Hongos
#  Enviar
#  Estado
#  Descripción
#    Una lluvia muy fuerte cae en el bosque Lua. Snorlex   un ansioso oso camba cazador de hongos decidió aprovechar su oportunidad e ir a cazarlos. Snorlex conoce un lindo camino que va a través del bosque que contiene varios claros donde hay un montón de hongos. Los claros consecutivos en el bosque son equidistantes entre sí. Snorlex necesita 15 minutos para caminar entre cualquier par de claros adyacentes. Habiendo arribado a un claro, Snorlex (como cualquier otro cazador de hongos respetable) recolecta todos los hongos de ese claro en un tiempo nulo. Es un hecho conocido que los hongos vuelven a crecer muy rápido y les toma sólo media hora para crecer de nuevo luego de que han sido recolectados. Sabiendo el número de hongos que crece en cada claro, la duración de la caminata de Snorlex y asumiendo que él elige una ruta que maximice su cosecha, encuentre el número de hongos que él recolectará. Snorlex puede terminar su caminata en cualquier punto del camino.
#   Entrada
#    La primera línea de la entrada contiene dos enteros: n y t (1<= n,t <= 1000000) los cuales denotan el número de claros en el camino y la duración de la caminata de Snorlex en cuartos (periodos de quince minutos). La segunda línea contiene una secuencia de n enteros ai (1<= ai <= 1000000), representando el número de hongos en cada claro del camino. Snorlex comienza su caminata en el primero de estos claros. Asumimos que Snorlex puede recolectar los hongos justo antes del primer cuarto y justo después del último cuarto (t-ésimo) de recolección.Para el ejemplo de abajo:
#    La primera línea de la entrada contiene dos enteros: n y t (1<= n,t <= 1000000) los cuales denotan el número de claros en el camino y la duración de la caminata de Snorlex en cuartos (periodos de quince minutos). La segunda línea contiene una secuencia de n enteros ai (1<= ai <= 1000000), representando el número de hongos en cada claro del camino. Snorlex comienza su caminata en el primero de estos claros. Asumimos que Snorlex puede recolectar los hongos justo antes del primer cuarto y justo después del último cuarto (t-ésimo) de recolección.
#    En la ruta más óptima de Snorlex, la cual le toma 60 minutos, él recolecta 18 hongos: 3 en un tiempo cero,  4 después de 15 minutos, 3 después de 30 minutos, 5 después de 45 minutos, y finalmente 3 después de 60 minutos.
#   Salida
#    En la primera y única línea de la salida tu programa debe entregar un entero: el máximo número de hongos que pueden ser recolectados durante la caminata de Snorlex.
#   Ejemplo Entrada
#    5 43 4 3 5 1
#   Ejemplo Salida
#    18
#   Ayuda
#    Simular el proceso

