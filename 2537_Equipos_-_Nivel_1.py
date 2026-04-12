# https://jv.umsa.bo/oj/problem.php?id=2537
#  Equipos - Nivel 1
#  Enviar
#  Estado
#  Descripción
#    Un día, tres mejores amigas, Diana, Fabiola y Cecilia, decidieron formar un equipo y participar en concursos de programación. A los participantes se les suelen ofrecer varios problemas durante los concursos de programación competitiva. Mucho antes del comienzo, las amigas decidieron que implementarán un problema si al menos dos de ellas están seguras de la solución. De lo contrario, no escribirán la solución del problema.
#    Este concurso de programación ofrece N problemas a los participantes. Para cada problema sabemos, cuál de las amigas está segura de la solución. Ayuda a las amigas a encontrar el número de problemas para los que escribirán una solución.
#   Entrada
#    La primera línea de entrada contiene un solo número entero N (1≤N≤1000) — que corresponde al número de problemas en el concurso. Las siguientes N líneas contienen tres enteros cada una, cada entero es 0 o 1. Si el primer número en la línea es igual a 1, entonces Diana está segura de la solución del problema, de lo contrario no está segura. El segundo número muestra la opinión de Fabi sobre la solución, el tercer número muestra la opinión de Ceci. Los números en las líneas están separados por espacios.
#   Salida
#    Imprime un solo número entero: la cantidad de problemas que las amigas implementarán en el concurso.
#   Ejemplo Entrada
#    31 1 01 1 11 0 0
#   Ejemplo Salida
#    2
#   Ayuda

n =  int(input())
s = 0
M = [[int(x) for x in input().split(' ')] for _ in range(n)]
for i in range(n):
    if M[i][0] + M[i][1] + M[i][2] > 1:
      s = s+1
print(s)