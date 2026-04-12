# https://jv.umsa.bo/oj/problem.php?cid=2824&pid=2
## https://jv.umsa.bo/oj/problem.php?id=2075
#  Among Us
#  Estado
#  Descripción
#    Among Us es un videojuego modo fiesta multijugador en línea, que consiste en hallar uno ó mas impostores.
#    Tu tarea sera hallar a los impostores.
#   Entrada
#    La entrada consiste de cinco lineas cada linea representa una habitacion del juego, en cada linea se te dara 3 nombres de los jugadores que estan en dicha habitacion. Luego de las cinco lineas se te dara un nombre $X$, nombre de la persona que se reporto.
#   Salida
#    Imprimir los nombres de los posibles sospechosos que estaban en la misma habitación donde estaba la persona que se reportó (imprimir en el mismo orden que la entrada).
#   Ejemplo Entrada
#    kay lupe alexandy ben wenmicky vale luchojimmy nomi anakenji rafa ivanlucho
#   Ejemplo Salida
#    micky vale
#   Ayuda
#    Condicionales
M = [list(input().split()) for _ in range(5)]
X = input()
for i in M:
    if X in i:
        i.pop(i.index(X))
        print(*i)
        break