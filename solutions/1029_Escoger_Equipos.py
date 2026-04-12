# https://jv.umsa.bo/oj/problem.php?id=1029
#  Escoger Equipos
#  Enviar
#  Estado
#  Descripción
#    Se tiene una lista de jugadores con los que conformaremos equipos. Se tiene de cada jugador unnúmero que califica su capacidad de juego. El número más grande representa un capacidad mayorPara escoger dos equipos se seleccionan dos capitanes, el primero naturalmente escoge al que juega mejor.Luego el segundo capitán escoge de los que quedan el que juega mejor y así sucesivamente.Veamos un ejemplo: los jugadores vienen como sigue: {5,7,8,4,2}, el primer capitán escogería el 8, el segundo el 7, así hasta que no queden jugadores. Con este proceso el equipo uno tendría a los jugadores con capacidad 8+5+2=15 y el segundo equipo 7+4=11. Se quiere mostrar en pantalla la diferencia en valor absoluto de ambas sumas 15-11=4
#   Entrada
#    La entrada consiste en múltiples casos de prueba. Cada caso de prueba contiene entre 1 y 50 números separados por un espacio en una línea. La entrada termina cuando no hay mas datos
#   Salida
#    Por cada caso de prueba escriba en la salida una línea con la diferencia en valor absoluto de la suma de la capacidad de juego.
#   Ejemplo Entrada
#    5 7 8 4 21001000 10009 8 7 61 5 10 1 5 10
#   Ejemplo Salida
#    4100020
#   Ayuda
#    ir tomando valores del mayor numero existentes y despues a sus predecesores

while True:
    try:
        A = list(map(int,input().split()))
        s = 0
        i = 1
        while len(A)>0:
            a=max(A)
            s+=a*i
            i*=-1
            A.pop(A.index(a))
        print(abs(s))
    except EOFError:
        break