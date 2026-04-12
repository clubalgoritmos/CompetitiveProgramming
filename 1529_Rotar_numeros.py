# https://jv.umsa.bo/oj/problem.php?cid=2825&pid=2
## https://jv.umsa.bo/oj/problem.php?id=1529
#  Rotar numeros
#  Enviar
#  Estado
#  Descripción
#    Se te dara un numero $x$ y tu tarea es rotar sus digitos $n$ veces a la izquierda.
#   Entrada
#    La entrada consiste de $T$ casos de prueba, para cada caso se te dara dos numeros enteros $x$ y $n$
#   Salida
#    La salida debera ser el numero $x$ rotado $n$ veces a la izquierda.
#   Ejemplo Entrada
#    271893 3123456 2
#   Ejemplo Salida
#    93718345612
#   Ayuda

for _ in range(int(input())):asd
    x, n = input().split()
    n = int(n) % (len(x))
    print(x[n:]+x[:n],sep="")