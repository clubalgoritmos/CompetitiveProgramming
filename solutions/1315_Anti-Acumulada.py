# https://jv.umsa.bo/oj/problem.php?id=1315
#  Anti-Acumulada
#  Enviar
#  Estado
#  Descripción
#    La acumulada de un vector V, denotado por Ac(V), es una vector A tal que todo A[i] es igual a V[0]+V[1]+V[2]+ ... + V[i].La anti-acumulada de un vector A es un vector V tal que Ac(V)=A.
#    Si V={ 1, 5, 0, -1 } entonces su vector acumulado es Ac(V)={ 1, 6, 6, 5}. Lo mismo{ 1, 5, 0, -1 } es la antiacumulada de{ 1, 6, 6, 5}.
#    Dado un vector A calcular los n elementos de su antiacumulada.
#   Entrada
#    En la primera líinea está un número n<=105. La sigueinte línea contine los valores A[0] A[1] ... A[n-1], tal que 0<=A[i]<=105.
#   Salida
#    Imprimir en una línea los valores de la anti-acumulada del vector de entrada. Imprimir un simple espacio en blanco entre cada elemento. No imprimir ningun espacio en blanco a la izquierda o derecha demás. No imprimir un fin de línea.
#   Ejemplo Entrada
#    53 6 7 5 3
#   Ejemplo Salida
#    3 3 1 -2 -2
#   Ayuda

n = int(input())
V = [0]
for x in input().split():
    x = int(x)
    V.append(abs(V[-1]-x))
print(V[1:])