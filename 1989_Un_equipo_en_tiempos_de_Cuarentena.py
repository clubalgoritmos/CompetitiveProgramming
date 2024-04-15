# https://jv.umsa.bo/oj/problem.php?cid=2824&pid=0
## https://jv.umsa.bo/oj/problem.php?id=1989
#  Un equipo en tiempos de Cuarentena
#  Estado
#  Descripción
#    Un día, tres mejores amigos, Daniel, Tonny y Alexander, decidieron formar un equipo y participar en concursos de programación de manera virtual. A los participantes generalmente se les ofrecen varios problemas durante los concursos de programación. Mucho antes del comienzo, los amigos en una reunión virtual decidieron que implementarían un problema si al menos dos de ellos están seguros de la solución. De lo contrario, los amigos no codificarán la solución del problema.
#    Este concurso ofrece $n$ problemas a los participantes. Para cada problema se sabe que uno de los tres estan seguros o no de la solución. Ayude a los amigos a encontrar la cantidad de problemas para los cuales codificaran una solución.
#   Entrada
#    La primera línea de entrada contiene un número entero $n$ ($1$ ≤ $n$ ≤ $100$): el número de problemas en el concurso. Le siguen n líneas que contienen tres enteros cada una, cada entero es 0 o 1. Si el primer número en la línea es igual a 1, entonces Daniel está segura de la solución del problema, si este número es igual a 0 no está seguro de la solución de este problema. El segundo número muestra la opinión de Tonny sobre la solución, el tercer número muestra la opinión de Alexander. Los números en las líneas están separados por espacios.
#   Salida
#    Imprima un número entero: la cantidad de problemas que los amigos implementarán (codificarán) en el concurso.
#   Ejemplo Entrada
#    41 1 00 0 11 1 10 0 0
#   Ejemplo Salida
#    2
#   Ayuda
#    Para el primer problema que les dan en el concurso, Daniel y Tonny están seguros de cómo resolver el problema, entonces este problema se codificara. Para el segundo problema sólo Alexander está seguro de la solución, no es suficiente para codificar. Para el tercer problema los tres saben cómo resolver el problema, esto significa que también este problema se codificara. Para el cuarto problema ninguno está seguro de la solución, no es suficiente para codificar. Por lo tanto los tres amigos sólo codificarán dos problemas (el primero y el tercero).
#    Para el cuarto problema ninguno está seguro de la solución, no es suficiente para codificar.
s=0
for _ in range(int(input())):
    s+=(sum(map(int,input().split()))>1)
print(s)