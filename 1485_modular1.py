# https://jv.umsa.bo/oj/problem.php?id=1485
## https://jv.umsa.bo/oj/problem.php?id=1485
#  modular1
#  Enviar
#  Estado
#  Descripción
#    Dado un lote de n números mostrar cuantos números son palíndromos utilizar almenos una función o procedimiento para realizar el ejercicio
#   Entrada
#    El problema tiene vario casos de prueba y termina cuando no hay mas datos.
#    Se debe leer un numero n de entrada el cual define cuantos numeros t habran para ser trabajados la entrada termina cuando no haya mas datos que leer
#   Salida
#    Por cada numero n leido de teclado debe haber una salida que indique cuatos nuemeros t son palindromos
#   Ejemplo Entrada
#    5131645112233443313322
#   Ejemplo Salida
#    2
#   Ayuda
#    Todos los números naturales son considerados para este ejercicio
while True:
    try:
        c=0
        for _ in range(int(input())):
            n = input()
            if n == n[::-1]:
                c += 1
        print(c)
    except EOFError:
        break