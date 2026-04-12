# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=60
## https://jv.umsa.bo/oj/problem.php?id=1346
#    Copiado al portapapeles
#  Neurona
#  Enviar
#  Estado
#  Descripción
#    Las neuronas son un tipo de células especiales que reaccionan a pequeños impulsos eléctricos. El cerebro está, entre otras cosas, compuesto de neuronas especializadas en la transmisión de información. En este problema vamos a estudiar el comportamiento de alguna neurona del cerebro de un ser vivo moribundo. Una neurona va muriendo por que las conexiones que tiene son muy débiles, y esto va produciéndose por a poco. Para la simplicidad del estudio se considera una neurona como un grafo conexo de n nodos y n-1 conexiones (no direccionadas) entre estas. Una neurona tarda una cierta cantidad de tiempo en morir. Se dice que una neurona muere cuando todos sus nodos han muerto.Si la neurona no ha muerto aun, entonces para el siguiente día todo nodo que sólo tenga conexión a otro muere para el día siguiente, es decir todo nodo con grado menos igual a 1.
#    En el grafo de la imagen el proceso va da la siguiente forma: Día 0. Al principio los nodos {1,2,3,4,5,6,7} están intactos.Día 1. Los nodos {1,3,5,7} mueren quedando sólo los nodos {2,4,6}.Día 2. Los nodos {2,6} mueren quedando sólo el nodo {4}.Día 3. El nodo {4} muere, entonces la neurona muere.
#   Entrada
#    La primera línea de entrada contiene la cantidad de nodos 1<=n<=100000 de la neurona a estudiar. Las siguiente n-1 lineas tienen dos enteros u y v, 1<=u,v<=n, que representan una conexión entre los nodos u y v. Se garantiza que la neurona será conexa.
#   Salida
#    Imprimir el número de día en los que la neurona muere.
#   Ejemplo Entrada
#    71 22 44 54 63 27 6
#   Ejemplo Salida
#    3
#   Ayuda

