# https://jv.umsa.bo/oj/problem.php?cid=2820&pid=3
## https://jv.umsa.bo/oj/problem.php?id=2321
#  Paseando
#  Enviar
#  Estado
#  Descripción
#    Fuiste de viaje y quieres conocer cuantos lugares puedes visitar.
#    La ciudad que fuiste es un rectángulo de x,y filas y columnas. Los lugares que puedes visitar están marcados por un punto. A los lugares marcados con
#    \#
#    no se puede ir. De un lugar marcado con punto puedes ir a otro lugar con punto.
#    Tu te encuentras en un lugar marcado con
#    @.
#    ¿A
#    cuantos lugares puedes ir incluyendo el lugar donde estas?
#   Entrada
#    La entrada consiste de múltiples casos de prueba. Cada caso de prueba comienza con dos números (
#    $2 \leq x,y \leq 10$
#    ). que representan las filas y columnas de la ciudad.
#    Luego siguen x filas cada una con y caracteres. La entrada de datos termina cuando x, y son cero.
#   Salida
#    En la salida escriba a cuantos lugares puede ir a visitar incluyendo en el que se encuentra.
#   Ejemplo Entrada
#    3 3....#..@.9 6....#......#..............................#@...#.#..#.0 0
#   Ejemplo Salida
#    845
#   Ayuda
while True:
    x,y = map(int,input().split())
    if x==0 and y == 0:
        break
    M = [list(input()) for i in range(x)]
    c = 1
    # a cuantos lugares puedo ir?
    for i in range(x):
        for j in range(y):
            if M[i][j] == "@":
                M[i][j] = c
                c += 1
    print(c)
