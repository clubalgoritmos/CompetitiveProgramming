# https://jv.umsa.bo/oj/problem.php?cid=2819&pid=2
## https://jv.umsa.bo/oj/problem.php?id=1674
#  Tarde de Cine
#  Enviar
#  Estado
#  Descripción
#    Un miercoles por la tarde, un grupo de amigos decidieron ver una película en el Cine.El grupo está compuesto de N miembros que recibieron cubos para nachos numerados de 1 a N.En un momento determinado, el cubo 1 tenía un nacho, el cubo 2 tenía dos nachos, y así sucesivamente hasta el cubo N, que tenía N nachos. Como son buenos amigos les gusta compartir, entonces decidieron simplificar las cosas, y decidieron juntar todas los nachos en un solo cubo.Procedieron de la siguiente manera: en el cubo 2, recogen las nachos de los cubos 1 y 2. Luego, en el cubo 3, los del cubo 2 y 3 y así sucesivamente hasta el último cubo. Formalmente, realizan n - 1 movimientos, en el i-ésimo movimiento que unen los nachos de los cubos i e i + 1 en el cubo i + 1. Sin embargo, se sabe que son torpes y en cada momento unen dos cubos, hacen caer al suelo un nacho, y la arrojan rápidamente a la basura.Uno de los integrantes del grupo se dio cuenta de que tal vez el último cubo sería demasiado pequeño para contener todos los nachos. Por lo tanto, necesita ayuda para determinar la cantidad de nachos que tendrá el último cubo segun el proceso descrito.Dado N, la cantidad de miembros que decidieron ver la película, se pide imprimir la cantidad de nachos que tendria el cubo N. Tenga en cuenta que exactamente un nacho se pierde en cada paso.
#   Entrada
#    La entrada consiste en un entero T (T<=100) que indica los casos de prueba, donde cada caso de prueba consiste en un unico numero entero N (2<=N<=109) que indica el numero de amigos que decidieron ver la pelicula.
#   Salida
#    Para cada caso de prueba se debe imprimir la cantidad de nachos que tendra el último cubo.
#   Ejemplo Entrada
#    323999999
#   Ejemplo Salida
#    24499998500002
#   Ayuda

for _ in range(int(input())):
    n = int(input())
    print(n*(n+1)//2-n+1)