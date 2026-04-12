# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=160
## https://jv.umsa.bo/oj/problem.php?id=1923
#    Copiado al portapapeles
#  Comprando dulces
#  Enviar
#  Estado
#  Descripción
#    Juan es un niño, como a todo niño le gustan los dulces, cuando caminaba por la calle vio $N$ tiendas dispuestas en un circulo enumeradas de $1, 2, ... , N$, como las tiendas vendian dulces fue inmediatamente hacia ellas, la tienda $i$ - ésima vende dulces a un precio $N_i$, cada tienda tiene un número ilimitado de dulces.
#    Juan tiene $K$ bolivianos, el desea gastar toda la plata si es necesario para adquirir dulces, para comprar algún dulce sigue los siguientes pasos.
#    Al principio, visita la tienda numero $1$.
#    Si tiene suficiente plata para comprar $un$ $dulce$de la tienda actual, entonces lo comprá inmediatamente.
#    Luego pasa a la siguiente tienda en orden de las agujas del reloj (independientemente si compro un dulce o no).
#    Como la cantidad de dinero que tiene Juan es finita, el proceso terminará en algún momento.
#    Calcule la cantidad de dulces que comprará Juan siguiendo los pasos anteriores.
#   Entrada
#    La primera linea contiene dos números enteros $N$ y $K$, $(1 \leq N \leq 2 * 10 ^ 5, 1 \leq K \leq 10 ^ {18})$ la cantidad de tiendas que hay y la cantidad de dinero que puede gastar Juan.
#    La segunda linea tiene $N$ enteros, $(1 \leq N_i \leq 10 ^ 9)$, cada entero denota el precio de un dulce en la $i$ - ésima tienda.
#   Salida
#    Imprime un entero que denota la cantidad de dulces que Juan puede comprar.
#   Ejemplo Entrada
#    3 71 3 1
#   Ejemplo Salida
#    5
#   Ayuda
#    Tienda $1$: compra $1$ dulce por $1$ Bs, entonces $K = 6$.
#    Tienda $2$: compra $1$ dulce por $3$ Bs, entonces $K = 3$.
#    Tienda $3$: compra $1$ dulce por $1$ Bs, entonces $K = 2$.
#    Tienda $1$: compra $1$ dulce por $1$ Bs, entonces $K = 1$.
#    Tienda $2$: no se puede comprar el dulce, ya que cuesta más del dinero que tiene.
#    Tienda $3$: compra $1$ dulce por $1$ Bs, entonces $K = 0$.

