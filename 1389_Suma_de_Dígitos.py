# https://jv.umsa.bo/oj/problem.php?id=1389
#  Suma de Dígitos
#  Enviar
#  Estado
#  Descripción
#    Escriba un programa que lea un número e imprima la suma de sus dígitos.
#    Escriba un programa que lea un número e imprima la suma de sus dígitos.
#    Escriba un programa que lea un número e imprima la suma de sus dígitos.
#   Entrada
#    La entrada consiste de varios números, cada número tiene mínimo un dígito y máximo $50$ dígitos. Cada número viene en una linea.La entrada termina cuando no hay más datos.
#    La entrada consiste de varios números, cada número tiene mínimo un dígito y máximo $50$ dígitos. Cada número viene en una linea.La entrada termina cuando no hay más datos.
#    La entrada consiste de varios números, cada número tiene mínimo un dígito y máximo $50$ dígitos. Cada número viene en una linea.La entrada termina cuando no hay más datos.
#   Salida
#    Para cada número imprima la suma de sus dígitos con el formato del ejemplo.
#    Para cada número imprima la suma de sus dígitos con el formato del ejemplo.
#    Para cada número imprima la suma de sus dígitos con el formato del ejemplo.
#   Ejemplo Entrada
#    291234567890123456789
#   Ejemplo Salida
#    La suma de los digitos de 29 es 11La suma de los digitos de 1234567890123456789 es 90
#   Ayuda
#    Puede sacar cada caracter para sumar su valor numerico
#    MULTIPLES CASOS DE PRUEBA EN PYTHON:
#    while True:  try:     #codigo  except EOFError:     break

while True:
    try:
        n = input()
        s = sum(list(map(int,n)))
        print(f"La suma de los digitos de {n} es {s}")
    except EOFError:
        break