# https://jv.umsa.bo/oj/problem.php?cid=2575&pid=1
## https://jv.umsa.bo/oj/problem.php?id=1052
#  Soltando Bolas
#  Estado
#  Descripción
#    Un numero de bolas son soltadas una por una desde la raiz de una estructura de un árbol binario (BST). Cada vez que una bola se suelta recorre por los nodos no terminales cayendo el sub árbol izquierdo o derecho hasta llegar a una hoja. Cuando llega a un nodo no terminal se levanta una bandera (con los valores true o false) que decide si debe caer a la izquierda o a la derecha. Inicialmente estas banderas tienen el valor false. Al llegar a un nodo terminal si la bandera es false primero cambia la bandera por true y luego cae por el lado izquierdo. En otros casos cambiara la bandera de true a false y bajara por el lado derecho. Todos los nodos del FTB están numerados comenzando en 1, nivel 1 (depth =1) y en dos nivel 2 (depth = 2) (vea el gráfico). Como ejemplo la figura 1, muestra un árbol un con profundidad cuatro con sus nodos números de 1 al 15. Como todos las banderas estarán en false, la primera bola que soltamos cambiara la bandera del nodo 1, 2 y 4 a true para finalmente quedar en la posición 8. La segunda bola cambiara las banderas 1, 3 y 6 para terminar en la posición 12. La tercera bola cambiara las banderas 1, 2 y 5 y terminara en la posición 10. Ahora considere un numero de casos de prueba donde se dan dos valores, la profundidad del árbol y el segundo valor que representa la I esima bola que se suelta. Debe asumir que I no excederá el numero total de las hojas del árbol.Escriba un programa para determinar la posición donde terminará la bola. La profundidad del árbol no será mayor a 20 y la I esima bola largada no es mayor a 524288.
#   Entrada
#    Ahora considere un numero de casos de prueba donde se dan dos valores, la profundidad del árbol y el segundo valor que representa la I esima bola que se suelta. Debe asumir que I no excederá el numero total de las hojas del árbol.Escriba un programa para determinar la posición donde terminará la bola. La profundidad del árbol no será mayor a 20 y la I esima bola largada no es mayor a 524288.
#   Salida
#    Por cada linea a la entrada escriba la posición donde terminara la bola.
#   Ejemplo Entrada
#    54 33 310 12 27 128
#   Ejemplo Salida
#    1055123127
#   Ayuda

