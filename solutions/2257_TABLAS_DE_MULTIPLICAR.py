# https://jv.umsa.bo/oj/problem.php?cid=2826&pid=20
## https://jv.umsa.bo/oj/problem.php?id=2257
#  TABLAS DE MULTIPLICAR
#  Enviar
#  Estado
#  Descripción
#    Juan es un niño de 9 años el cual le resulta muy difícil las matemáticas, y se le hace mucho más complicado al ser sus clases de manera virtual, en la escuela a Juan su profesor de matemáticas le pide que diga la tabla de cierto número x desde el 1 hasta n, y Juan busca una forma de aprender con ayuda de la programación. ¿Será que puedes ser capaz de ayudar a Juan con su problema?
#   Entrada
#    Dos números x, n ambos menores a 100
#   Salida
#    Los n números que corresponden a la solución del ejercicio
#   Ejemplo Entrada
#    5 6
#   Ejemplo Salida
#    5 10 15 20 25 30
#   Ayuda

x, n = map(int,input().split())
for i in range(1,n+1):
    print(x*i,end=" ")