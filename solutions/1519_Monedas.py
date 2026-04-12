# https://jv.umsa.bo/oj/problem.php?id=1519
#  Monedas
#  Enviar
#  Estado
#  Descripción
#    Dennis se aburrió de estudiar y se puso a jugar con su coleccion de monedas, y las ordenó de la siguiente forma:
#    Ahora el quizo descansar de las series que estuvo viendo, pero tal parece que el destino no lo quiere asi, por lo que aun jugando con sus monedas encuentra que podria haber una serie acá.
#    Dennis agrupará las monedas que necesita para realizar estas figuras, ahora tu tarea es decirle cuantas monedas hay en cada grupo.
#   Entrada
#    La primera línea es el valor de T, que son los casos a verificar.
#    Por cada caso de prueba, la entrada es un numero entero $n$ ($0 \leq n \leq 100$) que representa el número de figuras que Dennis quiere construir.
#   Salida
#    La salida consiste en $n$ numeros separados por un espacio que son cuantas monedas necesita para realizar las figuras de los tamaños desde $1$ hasta $n$
#   Ejemplo Entrada
#    253
#   Ejemplo Salida
#    1 6 15 28 451 6 15
#   Ayuda

generar_sucesion = lambda n: 1 if n<=0 else 1+(n)*4+generar_sucesion(n-1)
for _ in range(int(input())):
  print(*[generar_sucesion(i) for i in range(int(input()))])