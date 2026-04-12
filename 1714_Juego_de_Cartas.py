# https://jv.umsa.bo/oj/problem.php?id=1714
#  Juego de Cartas
#  Enviar
#  Estado
#  Descripción
#    Mientras espera el examen Dimitri se puso a jugar cartas. El juego es como sigue:Toma un conjunto de cartas y en cada una de ellas escribe un número. Ninguna carta tiene el mismo número. Luego va sacando una carta a la vez del mazo de cartas. Cada turno consiste en las siguientes acciones:Saca una carta arbitraria (al azar) del mazo de cartas. Sea $A$ el número escrito en la carta.
#    El juego termina cuando se terminan las cartas.Dado un conjunto de cartas devuelva el número máximo de turnos en que Dimitri puede tener para terminar el juego.
#   Entrada
#    La entrada esta compuesta por varios casos de prueba, cada caso de prueba comienza con un número entero $(1 \leq N \leq 50)$ que indica cuantas cartas tiene el mazo.Luego siguen $N$ cartas, cada una con un número $(1 \leq C \leq 499)$. Todos los números de las cartas son distintos. Termina cuando no hay más datos.
#   Salida
#    La salida consiste en una línea por cada caso de prueba con el número máximo de turnos para terminar el juego.
#   Ejemplo Entrada
#    2498 4996491 492 495 497 498 4994100 200 300 4001011 12 102 13 100 101 99 9 8 16118 321 322 119 120 3201410 11 12 13 14 1 2 3 4 5 6 7 8 9
#   Ejemplo Salida
#    144647
#   Ayuda

"""Juego de cartas"""

import sys

if __name__ == "__main__":
    for line in sys.stdin:
        lista = input()                 #leemos todo en una cadena
        lista = lista.split()           #lo convertimos en una lista
        lista2 = []
        for i in lista:
            lista2.append(int(i))       #convertimos cada elemento de la lista en un entero
        turno = 0
        lista2.sort()                   #ordenamos la lista
        for i in range(0, len(lista2)): #recorremos la nueva lista
            elemento = lista2[i]
            if elemento == 0:           #el cero representa que ya eliminamos un elemento (carta)
                continue
            else:                          #por condiciones del problema
                x = lista2.index(elemento)
                if x+1 < len(lista2):
                    if elemento+1 == lista2[x+1]:
                        lista2[x+1] = 0
                if elemento-1 == lista2[x-1]:
                    lista2[x+1] = 0
                lista2[x] = 0
                turno += 1
        print(turno)