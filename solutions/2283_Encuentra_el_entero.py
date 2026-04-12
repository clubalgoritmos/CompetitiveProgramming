# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=189
## https://jv.umsa.bo/oj/problem.php?id=2283
#    Copiado al portapapeles
#  Encuentra el entero
#  Enviar
#  Estado
#  Descripción
#    En este problema, su tarea es procesar varias consultas en la forma «comprobar si un número entero determinado está presente en el vector».
#   Entrada
#    La primera línea de entrada contiene dos números enteros $n$ y $m$ ($1 \leq n, m \leq 2⋅10^{5}$): el tamaño del vector y el número de consultas, respectivamente.
#    La siguiente línea contiene el vector: $n$ números enteros, cada uno de ellos no supera el valor absoluto de $10^{9}$. Puede suponer que los números enteros del vector se ordenan en orden creciente.
#    Cada una de las siguientes $m$ líneas describe una consulta y contiene un número entero que no excede el valor absoluto de $10^{9}$. Su tarea es verificar si este número entero está presente en el vector dado.
#   Salida
#    Para cada consulta, imprima "SI" en una nueva línea si el número entero de esta consulta existe en la matriz, o "NO" en caso contrario.
#   Ejemplo Entrada
#    5 10-11 -10 -2 11 18-211-101218-21518-20-18
#   Ejemplo Salida
#    SISISINOSISINOSINONO
#   Ayuda

n,m = map(int,input().split())
v = input()
for _ in range(m):
    x = input()
    print("SI" if x in v else "NO")
