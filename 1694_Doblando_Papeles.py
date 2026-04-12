# https://jv.umsa.bo/oj/problem.php?id=1694
#  Doblando Papeles
#  Enviar
#  Estado
#  Descripción
#    Un dia Sam estaba mirando los papeles y agarro una pieza rectangular de papel y dijo lo vamos a doblar de la siguiente manera:
#    Si lo desplegamos podriamos ver marcas del doblado del papel.
#   Entrada
#    Cada caso de prueba tendra un entero (1<=N<=25), cada caso de prueba indica cuantas veces quiere doblar Sam el pap
#   Salida
#    Por cada caso de prueba imprima una linea con el numero de caras que tiene el papel despues de desplegarlo.
#    Por cada caso de prueba imprima una linea con el numero de caras que tiene el papel despues de desplegarlo.
#   Ejemplo Entrada
#    1
#   Ejemplo Salida
#    2
#   Ayuda

n = int(input())
print(2**n)