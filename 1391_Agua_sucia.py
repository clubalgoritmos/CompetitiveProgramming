# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=74
## https://jv.umsa.bo/oj/problem.php?id=1391
#    Copiado al portapapeles
#  Agua sucia
#  Enviar
#  Estado
#  Descripción
#    Una empresa de agua sucia te ha contratado para que seas su contador. Esta empresa compra y vende turriles que tienen una cierta cantidad de litros de agua sucia. Como el mercado de venta y compra de agua sucia es muy competitivo quieren  saber en todo momento si son o no la mejor empresa de venta y compra de agua sucia. La empresa empieza con 0 turriles y se pondrá a comprar y vender turriles a lo largo del tiempo.El valor de la empresa en la bolsa de una empresa de agua sucia es igual a la multiplicación de las cantidades en litros de todos sus turriles, es decir, si tienen los turriles con cantidades de agua sucia en litros iguales a {1, 5, 2.5} entonces el valor en la bolsa de la empresa es igual a 1*5*2.5 = 12.5.La empresa sabe que es la mejor en su tipo si es que no puede existir otra empresa que tenga la misma cantidad de turriles, la misma cantidad total de agua (la suma en litros de todos los turriles) y tenga un mejor valor en la bolsa. Por ejemplo la empresa con los turriles {2.5, 2.5} es mejor en la bolsa que la empresa con los turriles {1, 4}.Tu trabajo es decidir despues de cada transacción si la empresa es la mejor o no.
#   Entrada
#    La primera línea de entrada contiene un entero T que representa el número de casos de prueba. A continuación se le da el valor de un entero N en una sola línea que representa la cantidad de transaccíones que la empresa realiza. La siguiente línea tiene N números enteros que representan una compra o venta en orden cronológico. Si uno de los números X es positivo significa que compraron un turril de X litros de agua sucia, al contrario, si este es negativo, representa que se vendió un turril de -X litros de agua. Se garantiza que una empresa no venderá un turril de una cantidad de litros de agua que no tenga y que la empresa jamás tendra cero turriles excepto al principio.
#   Salida
#    Imprimir en una línea una cadena de N caracteres que tenga en la posición i-ésima una letra S si es que la empresa es la mejor despues de la i-ésima transacción o una N si no es el caso.
#   Ejemplo Entrada
#    142 3 2 -3
#   Ejemplo Salida
#    SNNS
#   Ayuda

