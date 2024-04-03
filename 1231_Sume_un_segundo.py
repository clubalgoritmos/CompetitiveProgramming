# https://jv.umsa.bo/oj/problem.php?id=1231
#  Sume un segundo
#  Enviar
#  Estado
#  Descripción
#    Dadas las horas, minutos y segundos se le pide sumar un segundo.
#   Entrada
#    La entrada consiste de 3 números enteros separados por un espacio que representan las horas minutos y segundos. Donde horas < 24, minutos < 60 segundos < 60.
#   Salida
#    Imprima en la salida la nueva hora del reloj en formato mostrado en el ejemplo. Las horas, minutos y segundos deben estar en el siguiente formato:$$XX:YY:ZZ$$
#    Se debe poner ceros a la izquierda de los numeros si es necesario.
#   Ejemplo Entrada
#    11 33 15
#   Ejemplo Salida
#    11:33:16
#   Ayuda
#    #Para completar ceros a la izquierda en Python puede usar: print("{:02d}:{:02d}:{:02d}".format(a, b, c)) #Ejemplo:11:7:1 -> 11:07:01
#  #Para completar ceros a la izquierda en Python puede usar: print("{:02d}:{:02d}:{:02d}".format(a, b, c)) #Ejemplo:11:7:1 -> 11:07:01
#    #Para completar ceros a la izquierda en Python puede usar: print
#    "{:02d}:{:02d}:{:02d}"
#    ,
#    ,

a,b,c = map(int, input().split())
c+=1
if c>=60:
    c=0
    b+=1
    if b>=60:
        b=0
        a+=1
        if a>=24:
            a=0
print("{:02d}:{:02d}:{:02d}".format(a, b, c))