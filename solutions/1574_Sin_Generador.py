# https://jv.umsa.bo/oj/problem.php?id=1574
#  Sin Generador
#  Enviar
#  Estado
#  Descripción
#    Para todo entero positivo definiremos un generador como $d(n)$ que es $n$ mas la suma de sus dígitos. Por ejemplo $d(34))34+3+4=41$. De la misma manera podemos construir $d(d(34))=41+1+4=46$. Podemos construir infinitos números de la forma $d(d(d......d(n)))$.Algunos números no pueden construirse con este método, por ejemplo el 1,3,5.
#   Entrada
#    La entrada consiste en múltiples casos de prueba. Cada caso de prueba consiste en dos números positivos a,b ambos menores a 10000. La entrada termina cuando no hay más casos.
#   Salida
#    Por cada caso de entrada escriba en la salida cuantos números que no pueden construirse con este método y se encuentran entre a y b inclusive.
#   Ejemplo Entrada
#    1 103 95 202 99495000 9960
#   Ejemplo Salida
#    544978486
#   Ayuda

import sys

gen = []
for i in range(0, 100000):
    gen.append(0)


def sdigitos(n):                    #funcion recursiva para sumar digitos de un numero
    if n == 0:
        return 0
    else:
        return n % 10 + sdigitos(n // 10)


def generador(n):                   #funcion recursiva para generar
    c = n + sdigitos(n)
    if c <= 10000:
        if gen[c] != 1:
            gen[c] = 1
            generador(c)


for i in range(1, 9999):            #generamos los numeros
    generador(i)

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.split()         #leemos el rango
        s = 0
        for i in range(int(line[0]), int(line[1])+1):
            if gen[i] == 0:         #contamos los no generados
                s += 1
        print(s)