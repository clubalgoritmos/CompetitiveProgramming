# https://jv.umsa.bo/oj/problem.php?id=1728
#  sumar digitos pares
#  Enviar
#  Estado
#  Descripción
#    Dado un número x mayor a 1000, hallar la suma de sus dígitos pares
#    Dado un número x mayor a 1000, hallar la suma de sus dígitos pares
#   Entrada
#    La entrada consiste el multiples casos de prueba, cada línea tiene un numero entero n, positivo.
#    La entrada consiste el multiples casos de prueba, cada línea tiene un numero entero n, positivo.
#   Salida
#    Imprima la respuesta requerida en una sola línea.
#    Imprima la respuesta requerida en una sola línea.
#   Ejemplo Entrada
#    147222537
#   Ejemplo Salida
#    82
#   Ayuda
#    LECTURA DE MULTIPLES CASOS EN PYTHON
#    while True:   try:      #codigo   except EOFError:      break

while True:
    try:
        n=input().strip()
        print(sum(map(int,filter(lambda x: int(x)%2==0,n))))
    except Exception as e:
        break