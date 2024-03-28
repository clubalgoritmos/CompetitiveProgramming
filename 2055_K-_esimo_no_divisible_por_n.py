# https://jv.umsa.bo/oj/problem.php?id=2055
#  K- esimo no divisible por n
#  Enviar
#  Estado
#  Descripción
#    Dado dos enteros positivos n yk, Imprimir el k-esimo numero positivo que no sea divisible por n.
#    Por ejemplo.
#    si n = 3, y k =7 entonces todos los numeros no divisibles por 3 son [1,2,4,5,7,8,10,11,13,..]. La 7-iesima posicion es 10.
#   Entrada
#    El primer numero contiene un entero t (1<= t <= 1000) el numero de casos de prueba en la entrada.
#    Seguidos de t lineas.
#    Donde cada linea tiene dos enteros positivos n y k, (2<=n<=109) y (1<=k<=109)
#   Salida
#    Por cada linea imprimir los casos de prueba el k-esimo numero positivo que no sea divisible por n.
#   Ejemplo Entrada
#    63 74 122 10000000007 971000000000 10000000002 1
#   Ejemplo Salida
#    1015199999999911310000000011
#   Ayuda

for _ in range(int(input())):
    n,k = map(int,input().split())
    print(k+(k-1)//(n-1))