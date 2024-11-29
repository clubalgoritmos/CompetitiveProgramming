# https://jv.umsa.bo/oj/problem.php?cid=2826&pid=19
## https://jv.umsa.bo/oj/problem.php?id=2251
#  Rotaciones al Corte
#  Enviar
#  Estado
#  Descripción
#    Más difícil imposible dice Pepe al ver este problema, dado un número X y un dígito T, se le pidió rotar los primerosTdígitos empezando desde la derecha, el sentido para rotar dependerá si X es PAR rotar a la derecha Zdígitos, pero si X es IMPAR rotar a la izquierda Z dígitos, al terminar las rotaciones volver a componer el número original con la parte ya rotada, ayuda a Pepe a cumplir con su tarea.
#    Por ejemplo 456781635 los 4 números empezando por la derecha son: 1635 como X es impar se rotará 2 dígitos a la izquierda resultando 3516 y componiendo finalmente a 456783516.
#   Entrada
#    Son varios casos de prueba, cada caso se dará un (0 < X < 109), (1 < T <=log10X) y (1 <= Z <=9)
#   Salida
#    Por cada caso imprimir el número compuesto con los T números rotados Z veces.
#   Ejemplo Entrada
#    456781635 4 2890284184 2 6424812431 4 9142081417 6 2882952316 5 6
#   Ejemplo Salida
#    456783516890284184424814312142141708882965231
#   Ayuda

while True:
    try:
        X, T, Z = map(int,input().split())
        X = str(X)
        Y = X[T+1:]
        if int(Y)%2:
            Y = Y[(Z%len(Y)):]+Y[:(Z%len(Y))]
        else:
            Y = Y[:(Z%len(Y))]+Y[(Z%len(Y)):]
        print(X[:T+1],Y,sep="")
    except EOFError:
        break