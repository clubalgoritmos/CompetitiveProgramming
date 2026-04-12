# https://jv.umsa.bo/oj/problem.php?id=1585
#  Cortando un Cuadrado
#  Enviar
#  Estado
#  Descripción
#    Tienes un papel de N X N puesto sobre un plano de 2 dimensiones, los vértices del cuadrado se encuentran en los puntos (0,0), (0, N), (N, 0) y (N, N), primero el papel es cortado por 3 líneas horizontales y 3 líneas verticales, las líneas horizontales serán paralelas al eje x y las líneas verticales paralelas al eje y, dada cada línea en ¿Cuantas partes se divide el papel?
#    Tienes un papel de N X N puesto sobre un plano de 2 dimensiones, los vértices del cuadrado se encuentran en los puntos (0,0), (0, N), (N, 0) y (N, N), primero el papel es cortado por 3 líneas horizontales y 3 líneas verticales, las líneas horizontales serán paralelas al eje x y las líneas verticales paralelas al eje y, dada cada línea en ¿Cuantas partes se divide el papel?
#    Tienes un papel de N X N puesto sobre un plano de 2 dimensiones, los vértices del cuadrado se encuentran en los puntos (0,0), (0, N), (N, 0) y (N, N), primero el papel es cortado por 3 líneas horizontales y 3 líneas verticales, las líneas horizontales serán paralelas al eje x y las líneas verticales paralelas al eje y, dada cada línea en ¿Cuantas partes se divide el papel?
#    para el caso de prueba:
#    para el caso de prueba:
#   Entrada
#    La entrada contiene múltiples casos de prueba, cada caso de prueba contiene tres líneas, la primera línea contiene un entero N <= 100 (descrito en el enunciado) la segunda línea representando las rectas horizontales y la tercera línea las rectas verticales (<= 200).
#    La entrada contiene múltiples casos de prueba, cada caso de prueba contiene tres líneas, la primera línea contiene un entero N <= 100 (descrito en el enunciado) la segunda línea representando las rectas horizontales y la tercera línea las rectas verticales (<= 200).
#   Salida
#    Imprimir el número de partes en las que se dividirá el papel.
#    Imprimir el número de partes en las que se dividirá el papel.
#    Imprimir el número de partes en las que se dividirá el papel.
#   Ejemplo Entrada
#    35 1 32 3 5
#   Ejemplo Salida
#    4
#   Ayuda

# numeros Balanceados
import sys

if __name__ == '__main__':
    for line in sys.stdin:
        n = int(line)
        """Con esto fragmento lo que hacemos es leer las dos lineas
        con las rectas como son cadenas tenemos que convertirlas
        a enteros para luego ordenarlas"""
        i = input().split()
        j = input().split()
        X, Y = [], []
        for x in i:
            X.append(int(x))
        for y in j:
            Y.append(int(y))

        X.sort()
        Y.sort()
        """ una vez ordenados lo que procede es que contamos las rectas en este intervalo: ]0 , n[
        una vez que obtengamos la cantidad tanto en x como en y
        imcrementamos cada cantidad en 1 para asi obtener el resultado """
        rx = 0
        for i in X:
            if i > 0:
                if i >= n:
                    break
                else:
                    rx += 1
        ry = 0
        for i in Y:
            if i > 0:
                if i >= n:
                    break
                else:
                    ry += 1
        #son muchos for para esto
        #y todo por que la entrada no esta hecha para python :v
        print((rx + 1) * (ry + 1))