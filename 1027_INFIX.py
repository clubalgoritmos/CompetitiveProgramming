# https://jv.umsa.bo/oj/problem.php?id=1027
#  INFIX
#  Enviar
#  Estado
#  Descripción
#    La notación infix permite eliminar el uso de paréntesis en las expresiones aritméticas.
#    La forma en la que se escriben estas expresiones es como sigue:
#    a) primero escriba los operandos
#    b) luego escriba el operador
#    Por ejemplo, A B + significa hallar el resultado de A+B. El orden de proceso es el orden en que aparecen los símbolos.
#    En este problema los operadores validos serán los operadores aritméticos representados por letras S que representa la suma,  R la resta, D la división, M la multiplicación, y C elevar al cuadrado.
#   Entrada
#    El archivo de entrada consiste de varios casos de prueba. La primera linea de un caso de prueba es  el numero de casos existente. Cada caso de prueba viene en una linea, donde cada numero o operación esta separada por un espacio. Todos los números son enteros y todas las expresiones están bien formadas.
#   Salida
#    Escriba en una linea el resultado de evaluar la expresión.  El resultado es un número entero
#   Ejemplo Entrada
#    510 20 S10 C10 20 S 30 R 123 M6 20 D 3 M10
#   Ejemplo Salida
#    301000910
#   Ayuda

for _ in range(int(input())):
    r,l = None,None
    for arr in input().split():
        if arr=='S':
            r+=l
        elif arr=='M':
            r*=l
        elif arr=='D':
            r=l//r
        elif arr=='R':
            r-=l
        elif arr=='C':
            r=r**2
        elif r==None:
            r=int(arr)
        else:
            l=int(arr)
    print(r)