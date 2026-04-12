# https://jv.umsa.bo/oj/problem.php?id=1017
#  Cambio de Base
#  Enviar
#  Estado
#  Descripción
#    En la entrada nos darán dos números $n$ y $a$. Se conocen que el numero n convertido de decimal a un número en una de las bases $2,3,4,5,6,7,8,9$ iguala al numero a.Su trabajo es hallar la base B en la que esta el numero a
#   Entrada
#    La entrada consiste de varios casos de prueba. La primera línea contiene un numero (2 <= N <= 100) que indica el numero de casos de prueba.Luego siguen N lineas con en los números n y a descritos anteriormente.
#    Se garantiza que todos los datos entran en tipos de dato long en su respectivo lenguaje de programación.
#   Salida
#    Imprima la base en la que se encuentra $a$. Si existieran varias bases cumplen la propiedad imprima la menor de todas.
#   Ejemplo Entrada
#    2125 32545 231
#   Ejemplo Salida
#    64
#   Ayuda
#    la base de a no es menor ni igual al mayor digito de a

for _ in range(int(input())):
    n, a = map(int, input().split())
    for i in range(2, 10):
        x = a
        while x >= n:
            x //= i
        if x == n:
            print(i)
            break
    else:
        print("No solution")