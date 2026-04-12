# https://jv.umsa.bo/oj/problem.php?id=1591
#  Digitos Primos
#  Enviar
#  Estado
#  Descripción
#    Seremos simples y claros.
#    Se te dara un numero, y se te pide mostrar otro numero formado por los digitos primos de este.
#   Entrada
#    Se te dara un entero $T$ ($1 \leq T \leq 100$)que representara el numero de casos de prueba. Se te dara un numero $N$ ($1 \leq N \leq 10^{9}$)las siguientes T lineas
#   Salida
#    Para cada caso de prueba usted debe imprimir el nuevo numero conformado por los digitos primos del numero dado. En caso de que no exista ningun digito primo en un numero imprimir -1
#   Ejemplo Entrada
#    2122711111
#   Ejemplo Salida
#    227-1
#   Ayuda

for _ in range(int(input())):
    print("".join([i for i in input() if i in "2357"] or ["-1"]))