# https://jv.umsa.bo/oj/problem.php?cid=2826&pid=24
## https://jv.umsa.bo/oj/problem.php?id=2271
#  Principiante en divisiones.
#  Enviar
#  Estado
#  Descripción
#    Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no
#   Entrada
#    La primera línea indica cuántos casos de prueba tendremos.
#    Por cada caso de prueba se leen dos números a y b separados por un espacio ( 0≤a ) ( 0<b ).
#   Salida
#    Por cada caso de prueba se imprime un mensaje indicando si la división es exacta o no seguido del cociente y el resto de ser necesario.
#   Ejemplo Entrada
#    514 50 1512 320 114 3
#   Ejemplo Salida
#    La división no es exacta. Cociente: 2 Resto: 4La división es exacta. Cociente: 0La división es exacta. Cociente: 4La división es exacta. Cociente: 20La división no es exacta. Cociente: 4 Resto: 2
#   Ayuda

for _ in range(int(input())):
    a,b = map(int,input().split())
    if a%b:
        print("La división no es exacta. Cociente:",a//b,"Resto:",a%b)
    else:
        print("La división es exacta. Cociente:",a//b)