# https://jv.umsa.bo/oj/problem.php?id=1533
#  Impares y pares
#  Enviar
#  Estado
#  Descripción
#    A matilde le gusta mucho los numeros naturales (Numeros Enteros positivos).
#    Ella tiene los primeros N numeros natturales ordenados de una manera particular.
#    Primero tiene todos los numeros impares de 1 a N ordenados ascententemente y luego los
#    numero pares de 1 a N ordandos ascendentemente.
#    Ella quiere saber que numero estara en la posicion K
#   Entrada
#    La entrada consiste de varios casos de prueba.
#    Cada caso contiene dos numero enteros n y k 1 <= k <= n <= 10^12. La cantidad de de numeros que tiene matilde, k que numero se encuentra en la k esima exposcion.
#   Salida
#    Imprima el numero que queda en la K esima posicion.
#   Ejemplo Entrada
#    10 3
#   Ejemplo Salida
#    5
#   Ayuda
#    En el ejemplo tenemos 10 numero ordenados de la forma
#    1 3 5 7 9 2 4 6 8 10
#    k = 3
#    en la posicion 3 esta 5

# Pares Impares
import sys

if __name__ == "__main__":
    for datos in sys.stdin:
        datos = datos.split()
        n = int(datos[0])
        k = int(datos[1])
        if(n%2==0):
            if k > n//2:
                print((k - (n // 2)) * 2)
            else:
                print((k * 2) - 1)
        else:
            if k > (n//2) + 1:
                print((k - (n // 2)-1) * 2)
            else:
                print((k*2)-1)