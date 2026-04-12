# https://jv.umsa.bo/oj/problem.php?cid=2575&pid=2
## https://jv.umsa.bo/oj/problem.php?id=1148
#  Agregar
#  Estado
#  Descripción
#    El nombre del problema refleja la tarea, sumar un conjunto de números. Usted puede estar pensando en un programa que solo sume los números, pero hay una pequeña condición que hay que cumplir.  La operación de adición requiere un resultado "costo actual" que es la suma de los operandos. Por ejemplo si queremos sumar los elementos del conjunto $1$,$2$ y $3$ hay varias formas de hacerlo en pares de dos:
#    Forma 1$1 + 2 = 3$, costo actual $= 3$$3 + 3 = 6$, costo actual $= 6$Total $= 9$Forma 2 $1 + 3 = 4$, costo actual $= 4$$2 + 4 = 6$, costo $= 6$Total $= 10$Forma 3$2 + 3 = 5$, costo actual $= 5$$1 + 5 = 6$, costo actual $= 6$Total $= 11$
#    Espero que haya entendido nuestra misión y sumar el conjunto de enteros para que el costo sea mínimo.
#   Entrada
#    Cada caso de prueba comienza con un numero entero positivo $N$ ($2 \leq N \leq 10000$) seguido de $N$ números enteros positivos menores a $100000$. La entrada termina cuando el valor de $N$ es $0$.
#   Salida
#    Por cada caso de entrada imprima el costo mínimo de adición en una sola línea.
#   Ejemplo Entrada
#    31 2 341 2 3 40
#   Ejemplo Salida
#    919
#   Ayuda

import heapq

while True:
    n = int(input())
    if n == 0:
        break
    arr = list(map(int, input().split()))
    heapq.heapify(arr)
    total_cost = 0
    while len(arr) > 1:
        cost = heapq.heappop(arr) + heapq.heappop(arr)
        total_cost += cost
        heapq.heappush(arr, cost) 
    print(total_cost)