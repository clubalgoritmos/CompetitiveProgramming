# https://jv.umsa.bo/oj/problem.php?id=1093
#  Intercambio de Trenes
#  Enviar
#  Estado
#  Descripción
#    En una antigua estación de ferrocarril, usted todavía puede encontrar uno de los últimos intercambiadores de trenes. Un intercambiador de tren es un empleado del ferrocarril, cuya única función es la de reorganizar los vagones de los trenes.Una vez que los carros están organizados en el orden óptimo, el conductor del tren todo lo que tiene que hacer, es dejar los vagones, uno por uno, en las estaciones para las que corresponde la carga.El título intercambiadores de trenes}se deriva de la primera persona que llevó a cabo esta tarea, en una estación cerca de un puente del ferrocarril. En lugar de abrir verticalmente, el puente girar, sobre un pilar en el centro del río. Después de girar el puente de 90 grados, los barcos podían pasar a la izquierda o a la derecha.
#    El primer intercambiador de trenes había descubierto que el puente puede ser operado con un máximo de dos vagones en el. Al girar el puente de 180 grados, cambiado el lugar de los vagones, lo que le permite reorganizar los mismos (como efecto secundario, los vagones quedan en la dirección opuesta pero los vagones de tren se puede mover en cualquier dirección, así que le importa).Ahora que casi todos los intercambiadores de vagones han fallecido la compañía desea automatizar su operación. Parte del programa a ser desarrollado consiste en una rutina que decide, para< un tren dado, el numero de intercambios de dos vagones adyacentes, de tal forma de ordenar el tren. Su trabajo es crear esta rutina.
#   Entrada
#    La primera linea de la entrada es el numero de casos de prueba N. Cada caso de prueba consiste de dos lineas de entrada. La primera contiene un numero entero L que especifica la longitud del tren. La segunda linea segunda linea consiste de una permutación de números entre 1 y L, indicando el orden actual de los vagones. Los vagones deben ser ordenados de tal forma que el 1 viene antes del 2 y así sucesivamente, con el vagón L al final.
#   Salida
#    Para cada caso de prueba escriba un numero en una línea que representa el número óptimo de intercambio.
#   Ejemplo Entrada
#    331 3 244 3 2 122 1
#   Ejemplo Salida
#    161
#   Ayuda

for _ in range(int(input())):
    n = input()
    A = list(map(int,input().split()))
    c = 0
    while True:
        last = A.copy()
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                A[i],A[i+1] = A[i+1],A[i]
                c += 1
        if last==A:
            break
    print(c)