# https://jv.umsa.bo/oj/problem.php?id=1286
## https://jv.umsa.bo/oj/problem.php?id=1286
#  Pares incremento
#  Enviar
#  Estado
#  Descripción
#    Escriba un programa que lea una secuencia de números naturales tal que para cada secuencia imprima el numero de pares de números consecutivos talque el el segundo numero sea mayor que el primero.
#   Entrada
#    La entrada consiste de un numero natural n seguido de n secuencias. Cada secuencia termina con un cero.
#   Salida
#    Para cada secuencia imprima en una linea el numero de pares de numeros concecutivos, talque el segundo numero es mayor que el primero.
#   Ejemplo Entrada
#    31 2 3 4 04 4 3 3 2 2 1 1 06 8 4 4 5 0
#   Ejemplo Salida
#    302
#   Ayuda

for _ in range(int(input())):
    arr = list(map(int, input().split()))[:-1]
    count = 0
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            count += 1
    print(count)