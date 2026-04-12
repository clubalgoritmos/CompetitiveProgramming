# https://jv.umsa.bo/oj/problem.php?id=1335
#  Factorial Otra Vez
#  Enviar
#  Estado
#  Descripción
#    Mateo es un estudiante de ingeniera que esta desarrollando una forma original para representar numero enteros. El denomino este método "A Curious Method" cuya abreviación es ACM.La anotación ACM utiliza los mismos dígitos que la notación decimal, los dígitos del 0 al 9.Para convertir un numero A de la notación ACM a decimal usted debe adicionar k términos, donde k es el numero de dígitos del numero A en notación ACM. El valor del termino $i$ correspondiente al dígito $i$ contando de derecha a izquierda es $a_i \times i!$.Por ejemplo $719_{ACM}$ es equivalente a $53_{10}$, dado que $7 \times3!+ 1 \times 2! + 9 \times 1! = 53$.Mathews recién comienza sus estudios y desea que le ayudes a convertir los números en notación ACM a notación decimal.
#   Entrada
#    Cada caso de prueba esta dado en una linea que contiene un una cadena de un máximo de 5 dígitos, que representa el numero en notación ACM. la cadena no tiene ceros a la izquierda.El ultimo caso de prueba es una linea que contiene un cero.
#   Salida
#    Por cada caso de entrada imprima una linea conteniendo el numero decimal para la representación del numero ACM.
#   Ejemplo Entrada
#    7191151101020
#   Ejemplo Salida
#    531788
#   Ayuda

import sys

# Precomputar los factoriales
factorial = [1]
for i in range(1, 6):
    factorial.append(factorial[-1] * i)

for line in sys.stdin:
    N = line.strip()
    if N == '0':
        break
    N = N[::-1]  # Invertir la cadena para facilitar el cálculo
    decimal = sum(int(N[i]) * factorial[i + 1] for i in range(len(N)))
    print(decimal)