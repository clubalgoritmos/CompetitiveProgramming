# https://jv.umsa.bo/oj/problem.php?id=1903
#  Preguntar si una subcadena existe
#  Enviar
#  Estado
#  Descripción
#    El problema trata de averiguar si una subcadena existe en otra cadena
#    El problema trata de averiguar si una subcadena existe en otra cadena
#   Entrada
#    La entrada consiste en varios casos de prueba. La primera linea de cada caso de prueba contiene la primera cadena y la segunda la subcadena.
#    La entrada consiste en varios casos de prueba. La primera linea de cada caso de prueba contiene la primera cadena y la segunda la subcadena.
#   Salida
#    Por cada caso de entrada imprima la entrada imprima si existe o no existe la subcadena en la cadena como se muestra en el ejemplo.
#    Por cada caso de entrada imprima la entrada imprima si existe o no existe la subcadena en la cadena como se muestra en el ejemplo.
#   Ejemplo Entrada
#    2lagrancasadelpiscocasaclasesconeljuezpatitopases
#   Ejemplo Salida
#    sino
#   Ayuda

for _ in range(int(input())):
    S = input()
    s = input()
    if s in S:
        print("si")
        continue
    print("no")