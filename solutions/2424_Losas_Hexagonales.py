# https://jv.umsa.bo/oj/problem.php?cid=2575&pid=12
#  Losas Hexagonales
#  Estado
#  Descripción
#    Un camino conduce a la escuela de María. Se está pavimentando con losas hexagonales en una línea recta como se muestra en la imagen. María ama las matemáticas. Cuando va a la escuela, da pasos sobre las baldosas de ese camino con estas reglas:
#    Un camino conduce a la escuela de María. Se está pavimentando con losas hexagonales en una línea recta como se muestra en la imagen. María ama las matemáticas. Cuando va a la escuela, da pasos sobre las baldosas de ese camino con estas reglas:
#    Esta cerámica está siempre presente en EL INICIO de la ruta.
#    Las otras losas se numeran en
#    orden ascendente a partir del 1 de 1.
#    No se le permite regresar, es decir que no debe pisar una losa que lleva un número menor que en el que se encuentra. Por seguridad Siempre da pasos de una losa a la vecina.
#    El juego siempre termina en la baldosa con el número más alto.
#    uando terminan las clases ella está tan cansada que evita el camino y camina sobre el césped.
#    María no quiere repetir las secuencias de pasos sobre las losas y que le gustaría saber, si el camino es pavimentado con losas numeradas y una baldosa con la cara,
#    ¿Cuántos días se tardará en hacer cada posible secuencia de una vez.
#    ¿Cuántos días se tardará en hacer cada posible secuencia de una vez.
#   Entrada
#    La entrada comienza con el número el numero de casos de prueba.
#    La entrada comienza con el número el numero de casos de prueba.
#    La entrada contiene una línea por caso de prueba con el número $n$ de losas $1<n<10^{10}$.
#    La entrada contiene una línea por caso de prueba con el número $n$ de losas $1<n<10^{10}$.
#   Salida
#    Por cada línea de entrada escriba en la salida una línea es el número de secuencias modulo 1000000007.
#    Por cada línea de entrada escriba en la salida una línea es el número de secuencias modulo
#   Ejemplo Entrada
#    414210
#   Ejemplo Salida
#    15289
#   Ayuda

for _ in range(int(input())):
    N = int(input())
    print((2**N)//6 % 1000000007)