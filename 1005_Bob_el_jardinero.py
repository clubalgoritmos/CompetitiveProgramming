# https://jv.umsa.bo/oj/problem.php?id=1005
#  Bob el jardinero
#  Enviar
#  Estado
#  Descripción
#    'a' 'e' 'i' 'o' 'u'
#    Este problema esta pensado para que envie su solución en python, Para que sea aceptado debe escribir una función de redondeo que funcione tal como los hace el lenguaje Java o C,
#    Debe entender que diferentes lenguajes hacen el redondeo en forma diferente
#   Entrada
#   Salida
#   Ejemplo Entrada
#    3aeiouujigohavesup
#   Ejemplo Salida
#    Caso 1:a= 20.00e= 20.00i= 20.00o= 20.00u= 20.00Caso 2:a= 10.00e= 10.00i= 10.00o= 10.00u= 10.00Caso 3:a= 0.00e= 0.00i= 0.00o= 0.00u= 50.00
#   Ayuda
#    Una vez tengas la cantidad de frutas aplica la regla de 3 para obtener el porcentaje de cuantas frutas existe del tipo a,e,i,o,u
#    no dudes en usar otro tipo de almacenamiento para tus resultados puede que el int no sea suficiente para este ejercicio

import math

def round2(n):
    return math.floor(n * 100 + 0.5) / 100

T = int(input())

for _ in range(T):
    cadena = input().lower()
    a = cadena.count("a")
    e = cadena.count("e")
    i = cadena.count("i")
    o = cadena.count("o")
    u = cadena.count("u")
    total = len(cadena) - cadena.count(" ")
    print("Caso {0}:".format(_ + 1))
    print("a=", "{0:.2f}".format(round2((a * 100) / total)))
    print("e=", "{0:.2f}".format(round2((e * 100) / total)))
    print("i=", "{0:.2f}".format(round2((i * 100) / total)))
    print("o=", "{0:.2f}".format(round2((o * 100) / total)))
    print("u=", "{0:.2f}".format(round2((u * 100) / total)))