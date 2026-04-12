# https://jv.umsa.bo/oj/problem.php?id=1584
#  Botas y los museos
#  Enviar
#  Estado
#  Descripción
#    Botas planea visitar varios museos en un solo día, para ello tiene una lista de las ubicaciones de los museos, los museos se encuentran todos sobre una línea recta, ¿cuál será la mínima distancia que debe caminar botas si quiere visitar todos los museos?, él puede empezar y terminar su recorrido en cualquier punto de la recta.
#    Botas planea visitar varios museos en un solo día, para ello tiene una lista de las ubicaciones de los museos, los museos se encuentran todos sobre una línea recta, ¿cuál será la mínima distancia que debe caminar botas si quiere visitar todos los museos?, él puede empezar y terminar su recorrido en cualquier punto de la recta.
#    Por ejemplo:
#    Por ejemplo:
#    Botas puede empezar en el punto 1 y terminar en el punto 7, recorrerá una distancia de 6, de cualquier otra manera no se puede obtener una distancia menor
#    Botas puede empezar en el punto 1 y terminar en el punto 7, recorrerá una distancia de 6, de cualquier otra manera no se puede obtener una distancia menor
#    Botas puede empezar en el punto 1 y terminar en el punto 7, recorrerá una distancia de 6, de cualquier otra manera no se puede obtener una distancia menor
#   Entrada
#    La entrada consiste en varios casos de prueba, cada caso de prueba viene dado en dos líneas, la primera línea contiene un entero 1 <= N <= 100, la segunda línea contiene N enteros $a_i$ que indica que el museo i se encuentra en el punto $a_i$.
#    La entrada consiste en varios casos de prueba, cada caso de prueba viene dado en dos líneas, la primera línea contiene un entero 1 <= N <= 100, la segunda línea contiene N enteros $a_i$ que indica que el museo i se encuentra en el punto $a_i$.
#   Salida
#    Para cada caso imprimir la mínima distancia que puede recorrer botas.
#    Para cada caso imprimir la mínima distancia que puede recorrer botas.
#   Ejemplo Entrada
#    51 7 5 2 3
#   Ejemplo Salida
#    6
#   Ayuda

# Botas y los Museos
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        i = input().split()
        X = []
        for x in i:
            X.append(int(x))
        """Hemos leido los datos que que nos da, que sigue?
            Como cada museo es un punto del eje x
            entonces ordenamos los datos de menor a mayor
            de esta forma al restar el ultimo con el 
            primero tendremos la respuestta correcta"""
        X.sort()
        print(X[-1] - X[0])