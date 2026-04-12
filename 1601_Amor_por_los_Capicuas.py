# https://jv.umsa.bo/oj/problem.php?id=1601
#  Amor por los Capicuas
#  Enviar
#  Estado
#  Descripción
#    Un número capicua es aquel que se puede leer igual al derecho y al revez. por ejemplo 1221 es un numero capicua y 1232 no lo es. Ahora que ya sabes que son los numeros capicuas realiza un programa para identificar si es que un numero es o no capicua.
#   Entrada
#    La primera linea de entrada contendra un número N el cual es el número de casos de prueba, le siguen N lineas con numeros menores a 2000000000, 2 mil millones y siempre positivos.
#   Salida
#    Se deben imprimir N lineas con la palabra SI, si es que el número es capicua y la palabra NO, en caso contrario
#   Ejemplo Entrada
#    51221877887781232112111
#   Ejemplo Salida
#    SISINOSISI
#   Ayuda
#    Use el teorema fundamental de la numeracion


casos = int(input())
for i in range(casos):
    x =input()                  # si trabajamos con cadenas es mas facil
    if x == x[::-1]:            #X[::-1] es la cadena invertida de x
        print('SI')
    else:
        print('NO')