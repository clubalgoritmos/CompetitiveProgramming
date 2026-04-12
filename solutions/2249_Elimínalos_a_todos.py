# https://jv.umsa.bo/oj/problem.php?cid=2826&pid=18
## https://jv.umsa.bo/oj/problem.php?id=2249
#  Elimínalos a todos
#  Enviar
#  Estado
#  Descripción
#    Cuando un dígito quiere salirse de un número más grande quiere irse causando caos, se dará un númeo X, a este se le deberá quitar todos los dígitos que sean iguales a un dígito D, pero quitando a D se deberá reemplazar con el número de una cifra más grande que tenga X, si D es la cifra más grande reemplazar por el segundo más grande.
#   Entrada
#    Son varios casos de prueba cada caso se dará un X (102 < Z <= 109) y un D (0 < D < 10)
#   Salida
#    Por cada caso imprimir el nuevo número sin tener ningún D.
#   Ejemplo Entrada
#    1232545687 598762165499 913036728 749732364 33794308 711480296 6
#   Ejemplo Salida
#    1232848687887621654881303682849792964399430811480299
#   Ayuda
while True:
    try:
        X, D = input().split()
        for x in X:
            if x == D:
                X = X.replace(x, str(max([int(i) for i in X if i != D])))
        print(X)
    except EOFError:
        break
