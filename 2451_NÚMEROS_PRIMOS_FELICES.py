# https://jv.umsa.bo/oj/problem.php?cid=2567&pid=2
#  NÚMEROS PRIMOS FELICES
#  Estado
#  Descripción
#    Un nùmero primo es un número natural mayor que uno, que tiene únicamente dos divisores positivos: el mismo número y el número uno.
#    Un nùmero primo es un número natural mayor que uno, que tiene únicamente dos divisores positivos: el mismo número y el número uno.
#    Por otro lado unnúmero felizse define por el siguiente procedimiento: empezando con cualquiernúmeroentero positivo, se reemplaza elnúmeropor la suma de los cuadrados de sus dígitos, y se repite el proceso hasta que elnúmeroes igual a 1 o hasta que se entra en un bucle que no incluye el 1. Por tanto, aquellos números que al finalizar el proceso terminan en uno son conocidos como números felices.
#    Por otro lado un
#    se define por el siguiente procedimiento: empezando con cualquier
#    entero positivo, se reemplaza el
#    por la suma de los cuadrados de sus dígitos, y se repite el proceso hasta que el
#    es igual a 1 o hasta que se entra en un bucle que no incluye el 1. Por tanto, aquellos números que al finalizar el proceso terminan en uno son conocidos como números felices.
#   Entrada
#    La entrada consiste en un número entero positivo n entre 1 y 1000
#    La entrada consiste en un número entero positivo n entre 1 y 1000
#   Salida
#    Si el número n es primo y feliz se imprime el siguiente mensaje: Primo Feliz
#    Si el número n es primo y feliz se imprime el siguiente mensaje: Primo Feliz
#    Si el número n es primo e infeliz, se imprime el siguiente mensaje: Primo Infeliz
#    Si el número n es primo e infeliz, se imprime el siguiente mensaje: Primo Infeliz
#    Si el número n no es primo, se imprime el siguiente mensaje: No es Primo
#    Si el número n no es primo, se imprime el siguiente mensaje: No es Primo
#   Ejemplo Entrada
#    7
#   Ejemplo Salida
#    Primo Feliz
#   Ayuda

x=int(input())
if x%2==0:
    print("No es Número Primo")
else:
    if len(str(x))==1:
        ylist = [int(y) for y in list(str(x*x))]
    else:
        ylist = [int(y) for y in list(str(x))]
    y = 0
    while sum(ylist) !=1:
        rel = (ylist[0]*ylist[0]) + (ylist[1]*ylist[1])
        ylist = [int(y) for y in list(str(rel))]
        y = y+1
        if y > 10:
            print("Número Primo Infeliz")
            break
           
    if sum(ylist) == 1:
        print("Número Primo Feliz")