# https://jv.umsa.bo/oj/problem.php?id=1299
#  Producto Escalar
#  Enviar
#  Estado
#  Descripción
#    El producto escalar de dos vectores $A={a_1,a_2,a_3,.....a_n}$, $B={b_1,b_2,b_3,...b_n}$ se define como \[AxB=\sum_{i=1}^n a_i b_i\]]
#   Entrada
#    La primera linea especifica el numero de casos de prueba. Cada caso de prueba consiste de vectores A y B. La primera linea de cada vector el numero elementos del vector. Luego siguen dos lineas la primera con los elementos del vector A y la segunda con los elementos del vector B.
#   Salida
#    En la salida imprima el producto escalar de cada caso de prueba.
#   Ejemplo Entrada
#    2102 5 10 5 5 7 4 6 9 5 9 7 8 2 3 9 3 10 7 5 107 2 10 4 6 9 9 5 6 10 5 8 9 8 2 6 6 5 9 10
#   Ejemplo Salida
#    381472
#   Ayuda
#    dos vectores del mismo tamaño

for _ in range(int(input())):
    N = input()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    s = 0
    for a,b in zip(A,B):
        s += a*b
    print(s)