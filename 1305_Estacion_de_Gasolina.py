# https://jv.umsa.bo/oj/problem.php?cid=2819&pid=9
## https://jv.umsa.bo/oj/problem.php?id=1305
#  Estacion de Gasolina
#  Enviar
#  Estado
#  Descripción
#    Un conductor de automóvil necesita un plan para recorrer una carretera. Cuando el tanque de gasolina de su automóvil esta lleno el puede recorrer a lo mucho X km. El conoce la localización de las N estaciones de gasolina en la carretera, ahora el conductor necesita saber cual es el mínimo numero de paradas que tiene que hacer para recorrer a lo mínimo D km?Vamos asumir que inicialmente el carro esta con el tanque lleno de gasolina.
#   Entrada
#    La entrada viene seguida por varios casos de prueba. La primera linea de cada uno de los casos de prueba tiene dos enteros X y D  con (0<D,X<=10⁹). La segunda linea viene dada por N las estaciones de servicio que tenemos con (0<N<=10⁵), seguidamente n números que indican la distancia a la que se encuentran del punto de partida, vamos sumir que todas las distancias son diferentes y que están en el rango de 1<=ni<D. Para todos los casos siempre es posible recorrer los D km.
#   Salida
#    Por cada caso la salida en una linea indicando la cantidad mínima de paradas para recorrer los D km.
#   Ejemplo Entrada
#    2 53 1 3 43 104 1 8 6 415 106 5 2 9 4 1 3
#   Ejemplo Salida
#    240
#   Ayuda
while True:
    try:
        X, D = map(int,input().split())
        N, *A = map(int,input().split())
        A.sort()
        A = [0] + A
        
        c = 0
        last_stop = D
        for i in range(len(A)-1, 0, -1):asdasd
            if last_stop - A[i] >= X:
                last_stop = A[i]
                c += 1
        print(c)
    except EOFError:
        break