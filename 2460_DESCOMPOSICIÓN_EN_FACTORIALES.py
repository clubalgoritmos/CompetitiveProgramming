# https://jv.umsa.bo/oj/problem.php?cid=2567&pid=5
#  DESCOMPOSICIÓN EN FACTORIALES
#  Estado
#  Descripción
#    Se define al factorial de un número N, como el producto de todos los números entre 1 y N:
#    Se define al factorial de un número N, como el producto de todos los números entre 1 y N:
#    N! = 1 x 2 x 3 x ... x (N-1) x N
#    N! = 1 x 2 x 3 x ... x (N-1) x N
#    Dado un número entero positivo N, escribe un programa que determine el número K más pequeño tal que, N=t1!+t2!+t3!+...+tk!, donde cada ti es un número entero positivo.
#    Dado un número entero positivo N, escribe un programa que determine el número K más pequeño tal que, N=t1!+t2!+t3!+...+tk!, donde cada ti es un número entero positivo.
#    Por ejemplo, cuando N=10 la respuesta es 3, porque es posible escribir 10 como la suma de 3 números factoriales: 10 = 3! + 2! + 2!.
#    Por ejemplo, cuando N=10 la respuesta es 3, porque es posible escribir 10 como la suma de 3 números factoriales: 10 = 3! + 2! + 2!.
#    Otro ejemplo, cuando N=25, la respuesta es 2, porque es posible escribir 25 como la suma de 2 números factoriales: 25 = 4! + 1!
#    Otro ejemplo, cuando N=25, la respuesta es 2, porque es posible escribir 25 como la suma de 2 números factoriales: 25 = 4! + 1!
#   Entrada
#    La entrada consiste de una única línea que contiene un entero N (1 <= N <= 105)
#    La entrada consiste de una única línea que contiene un entero N (1 <= N <= 105)
#   Salida
#    La salida consiste de un único valor que representa la cantidad mínima de números factoriales que suman N
#    La salida consiste de un único valor que representa la cantidad mínima de números factoriales que suman N
#   Ejemplo Entrada
#    25
#   Ejemplo Salida
#    2
#   Ayuda

n=int(input())
factoriales = [1]
i = 1
while factoriales[-1] <= n:
    i += 1
    factoriales.append(factoriales[-1] * i)
factoriales.pop()
contador = 0
for f in reversed(factoriales):
    while n >= f:
        n -= f
        contador += 1
print(contador)
