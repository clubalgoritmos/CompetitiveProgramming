# https://jv.umsa.bo/oj/problem.php?id=1312
#  Comprando
#  Enviar
#  Estado
#  Descripción
#    Steve desea comprar un coche nuevo. No es rico por lo que el preferirá un coche razonablemente barato. El único inconveniente es que la calidad de los coches baratos es cuestionable. Así, Steve decide hacer una lista de precios de los automóviles de donde escogerá el coche con el tercer precio más bajo.
#    Steve desea comprar un coche nuevo. No es rico por lo que el preferirá un coche razonablemente barato. El único inconveniente es que la calidad de los coches baratos es cuestionable.
#    Así, Steve decide hacer una lista de precios de los automóviles de donde escogerá el coche con el tercer precio más bajo.
#    Se lee un vector de enteros con los precios. Un precio se puede repetir varias veces en la lista de precios, pero debe contar como una sola vez.
#    Escribe un programa que devuelve el tercer precio más bajo de la lista. Si hay menos de tres precios diferentes el resultado es $-1$.
#   Entrada
#    La entrada consiste de varios casos de prueba. La primera línea de cada caso de prueba contiene el número de precios coches $1< N \leq 50$. La siguiente línea contiene $0 < N \leq 1000$ números que representan la lista de precios. La entrada termina cuando no hay más datos.
#   Salida
#    Imprima para cada caso de prueba el tercer precio menor de la lista.
#   Ejemplo Entrada
#    910  40  50  20  70  80  30  90  601010  10  10  10  20  20  30  30  40  40110580  90  80  90  80
#   Ejemplo Salida
#    3030-1-1
#   Ayuda
#    comparar los elementos con algun metodo de busqueda usando un contador

while True:
    try:
        n = input()
        A = sorted(set(map(int,input().split())))
        print(A[2] if len(A)>2 else -1)
    except EOFError:
        break