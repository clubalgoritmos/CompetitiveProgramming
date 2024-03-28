# https://jv.umsa.bo/oj/problem.php?id=1486
#  modular2
#  Enviar
#  Estado
#  Descripción
#    Realizar la siguiente serie 1, 2, 1, 4, 2, 6, 3, 8, 5, 10, 8, 12 hasta n (aplicar funciones o procedimientos)
#   Entrada
#    La entrada consiste en un numero n entero positivo la entrada termina cuando no hay mas datos que leer
#   Salida
#    La salida consiste en la muestra de la serie hasta n elementos
#   Ejemplo Entrada
#    8
#   Ejemplo Salida
#    12142638
#   Ayuda
#    Se puede realizar una funcion o procedimiento para realizar la serie si cree que la serie es la union de 2 entonces una funcion o procedimiento para cada una

n = int(input())
i = 1
fibo = [1,0]
while i<=n:
    if i%2==0:
        print(i)
    else:
        fibo.append(fibo[-1]+fibo[-2])
        fibo.pop(0)
        print(fibo[-1])
    i+=1
