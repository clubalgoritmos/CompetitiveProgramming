# https://jv.umsa.bo/oj/problem.php?id=1530
#  Cambio de numero
#  Enviar
#  Estado
#  Descripción
#    Los habitantes de Letropolis estan en busca de nuevas formas de atraer turistas a su ciudad y decidieron que una de sus avenidas principales pasara a llamarese Av. Primos, con la particuliaridad que todas los numeros de las casas de esta avenida estan formados por solamente digitos primos, entonces te piden ayuda para cambiar los antiguos numeros de las casas por los nuevos que se piden.
#    Los habitantes de Letropolis estan en busca de nuevas formas de atraer turistas a su ciudad y decidieron que una de sus avenidas principales pasara a llamarese Av. Primos, con la particuliaridad que todas los numeros de las casas de esta avenida estan formados por solamente digitos primos, entonces te piden ayuda para cambiar los antiguos numeros de las casas por los nuevos que se piden.
#    Los habitantes de Letropolis estan en busca de nuevas formas de atraer turistas a su ciudad y decidieron que una de sus avenidas principales pasara a llamarese Av. Primos, con la particuliaridad que todas los numeros de las casas de esta avenida estan formados por solamente digitos primos, entonces te piden ayuda para cambiar los antiguos numeros de las casas por los nuevos que se piden.
#    Entonces ellos te dirán cuantas casas existen en la avenida, y luego el número antiguo que estas tenian, tu tarea es devolver su nuevo numero formado solo por digitos primos:
#    Entonces ellos te dirán cuantas casas existen en la avenida, y luego el número antiguo que estas tenian, tu tarea es devolver su nuevo numero formado solo por digitos primos:
#    Entonces ellos te dirán cuantas casas existen en la avenida, y luego el número antiguo que estas tenian, tu tarea es devolver su nuevo numero formado solo por digitos primos:
#    Por ejemplo si una casa tenia el numero $7854215$ su nuevo número sera $7525$ ya que es el numero que queda al quitar todos los digitos que no son primos.
#    Por ejemplo si una casa tenia el numero $7854215$ su nuevo número sera $7525$ ya que es el numero que queda al quitar todos los digitos que no son primos.
#    Por ejemplo si una casa tenia el numero $7854215$ su nuevo número sera $7525$ ya que es el numero que queda al quitar todos los digitos que no son primos.
#    Si no se puede hacer lo anterior responder $0$
#    Si no se puede hacer lo anterior responder $0$
#    Si no se puede hacer lo anterior responder $0$
#   Entrada
#    La entrada consiste en un numero entero $t$ que sera el número de casas de la avenida. (Casos de prueba)
#    La entrada consiste en un numero entero $t$ que sera el número de casas de la avenida. (Casos de prueba)
#    La entrada consiste en un numero entero $t$ que sera el número de casas de la avenida. (Casos de prueba)
#    Por cada casa se te dara un numero entero $n$ ($1 \leq n \leq 10^{9}$) que es el antiguo número de la casa.
#    Por cada casa se te dara un numero entero $n$ ($1 \leq n \leq 10^{9}$) que es el antiguo número de la casa.
#    Por cada casa se te dara un numero entero $n$ ($1 \leq n \leq 10^{9}$) que es el antiguo número de la casa.
#   Salida
#    La salida consiste de un numero entero por cada casa, que representa el nuevo número de esa casa, si la casa no puede tener un numero formado por solo digitos primos se debe imprimir $0$.
#    La salida consiste de un numero entero por cada casa, que representa el nuevo número de esa casa, si la casa no puede tener un numero formado por solo digitos primos se debe imprimir $0$.
#    La salida consiste de un numero entero por cada casa, que representa el nuevo número de esa casa, si la casa no puede tener un numero formado por solo digitos primos se debe imprimir $0$.
#   Ejemplo Entrada
#    478542151234561468927
#   Ejemplo Salida
#    7525235027
#   Ayuda

primes = set([2,3,5,7])

def filter_primes(n):
    digits = map(int, str(n))
    filtered = list(filter(primes.__contains__, digits))
    return filtered if filtered else [0]

for _ in range(int(input())):
    print(*filter_primes(input()), sep='', end='\n'):