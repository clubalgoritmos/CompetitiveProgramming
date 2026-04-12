# https://jv.umsa.bo/oj/problem.php?cid=2567&pid=3
#  CALCULANDO EL PESO DEL BUSCAMINAS
#  Estado
#  Descripción
#    Buscaminas es un juego entretenido cuyo objetivo es encontrar todas las minas ubicadas en un campo de dimensionesM×N.
#    Buscaminas es un juego entretenido cuyo objetivo es encontrar todas las minas ubicadas en un campo de dimensiones
#    M
#    ×
#    N
#    .
#    El juego muestra un número en un recuadro que indica la cantidad de minas adyacentes a ese recuadro. Cada recuadro tiene, como mucho, ocho recuadros adyacentes, arriba, abajo, izquierda, derecha y las cuatro diagonales.
#    El juego muestra un número en un recuadro que indica la cantidad de minas adyacentes a ese recuadro. Cada recuadro tiene, como mucho, ocho recuadros adyacentes, arriba, abajo, izquierda, derecha y las cuatro diagonales.
#    En el ejemplo, de tamaño4×4, a la izquierda contiene dos minas, cada una de ellas representada por el carácter∗. Si representamosel mismo campo con los siguientes números:
#    En el ejemplo, de tamaño
#    4×4
#    ,
#    a la izquierda contiene dos minas, cada una de ellas representada por el carácter
#    ∗
#    . Si representamosel mismo campo con los siguientes números:
#    9 representa a la mina y los valores 1 al 8 el valor de las minas adyacentes. El peso es la sumatoria de todos los números obtenidos al finalizar la identificación de las minas.
#    9
#    representa a la mina y los valores 1 al 8 el valor de las minas adyacentes. El peso es la sumatoria de todos los números obtenidos al finalizar la identificación de las minas.
#    *...    9000  9100
#    *...    9000  9100
#    ....    0000   2210
#    ....    0000   2210
#    .*..    0900  1910 Peso = 29
#    .*..    0900  1910 Peso
#    = 29
#    ....    0000   1110
#    ....    0000   1110
#   Entrada
#    La entrada consta de un número arbitrario de campos. La primera línea de cada campo consta
#    La entrada consta de un número arbitrario de campos. La primera línea de cada campo consta
#    de dos números enteros, n y m (0≤n,m≤1000), que representan, respectivamente, el número de líneas y columnas del campo. Cada una de las siguientes n líneas contiene, exactamente, m caracteres, que describen las minas (*) y los espacios vacíos (.).
#    de dos números enteros, n y m (
#    0≤
#    n
#    ,
#    m
#    ≤100
#    0
#    ), que representan, respectivamente, el número de líneas y columnas del campo. Cada una de las siguientes n líneas contiene, exactamente, m caracteres, que describen las minas (*) y los espacios vacíos (.).
#   Salida
#    Un número entero que representa el PESO, que es el cálculo de la sumatoria de los números obtenidos después de calcular los valores respectivos.
#    Un número entero que representa el PESO, que es el cálculo de la sumatoria de los números obtenidos después de calcular los valores respectivos.
#   Ejemplo Entrada
#    4 4*........*......
#   Ejemplo Salida
#    29
#   Ayuda

F,C=map(int,input().split())
S = 0
M = [list(input()) for _ in range(F)]

for i in range(F):
    for j in range(C):
        if M[i][j]=="*":
            if i-1>=0 and M[i-1][j]!="*":
                S+=1
            if i+1<F and M[i+1][j]!="*":
                S+=1
            if j-1>=0 and M[i][j-1]!="*":
                S+=1
            if j+1<C and M[i][j+1]!="*":
                S+=1
            if i-1>=0 and j-1>=0 and M[i-1][j-1]!="*":
                S+=1
            if i-1>=0 and j+1<C and M[i-1][j+1]!="*":
                S+=1
            if i+1<F and j-1>=0 and M[i+1][j-1]!="*":
                S+=1
            if i+1<F and j+1<C and M[i+1][j+1]!="*":
                S+=1
            S+=9
print(S)