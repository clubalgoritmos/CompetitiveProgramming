# https://jv.umsa.bo/oj/problem.php?id=1089
#  Epicentro
#  Enviar
#  Estado
#  Descripción
#    El epicentro de un número n es el dígito que está en el medio del número.
#    El epicentro de un número n es el dígito que está en el medio del número.
#    Por ejemplo el epicentro de 89012 es 0 porque es el dígito que está en la mitad del número.
#    Por ejemplo el epicentro de 89012 es 0 porque es el dígito que está en la mitad del número.
#    Algunos números no tienen epicentro es el caso de los números con cantidad de dígitos par.
#    Algunos números no tienen epicentro es el caso de los números con cantidad de dígitos par.
#    Por ejemplo el número 2244 no tiene epicentro porque su cantidad de dígitos es 4.
#    Por ejemplo el número 2244 no tiene epicentro porque su cantidad de dígitos es 4.
#    Dado un número, se quiere encontrar cuál es su epicentro.
#    Dado un número, se quiere encontrar cuál es su epicentro.
#   Entrada
#    La primera linea contiene el numero de casos de prueba. luego sigue en cada caso de prueba una linea con un numero entre 1 y $10^20$.
#   Salida
#    Según sea la entrada se pide imprimir el dígito epicentro en una línea, si el epicentro no existiera se deberá imprimir "*" sin comillas.
#   Ejemplo Entrada
#    3112322
#   Ejemplo Salida
#    12*
#   Ayuda

for _ in range(int(input())):
    S = input()
    if len(S)%2==0:
        print("*")
        continue
    print(S[len(S)//2])