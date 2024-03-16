# https://jv.umsa.bo/oj/problem.php?id=1046
#  Adivine la Estructura
#  Enviar
#  Estado
#  Descripción
#    Una estructura de datos es similar a una bolsa soporta $2$ operaciones:
#    Una estructura de datos es similar a una bolsa soporta $2$ operaciones:
#    Una estructura de datos es similar a una bolsa soporta $2$ operaciones:
#    $1$ $x$:
#    $1$ $x$:
#    Inserta un elemento a la bolsa (comando de tipo1)
#    Inserta un elemento a la bolsa (comando de tipo1)
#    $2$ $x$:
#    $2$ $x$:
#    Saca un elemento de la bolsa (comando de tipo2)
#    Saca un elemento de la bolsa (comando de tipo2)
#    Dada una secuencia de operaciones con valores de retorno usted de decir que estructura de datos se utilizó. Hay tres estructuras de datos:
#    Dada una secuencia de operaciones con valores de retorno usted de decir que estructura de datos se utilizó. Hay tres estructuras de datos:
#    Dada una secuencia de operaciones con valores de retorno usted de decir que estructura de datos se utilizó. Hay tres estructuras de datos:
#    1) Pila (ultimo en entrar el  primero en salir).2) Cola de prioridad  (siempre sacar el elemento más grande primero).3)  Cola  (primero en entrar el primero en salir).4) O algo que no puede imaginar
#    1)
#    1)
#    Pila (ultimo en entrar el  primero en salir).2) Cola de prioridad  (siempre sacar el elemento más grande primero).3)  Cola  (primero en entrar el primero en salir).4) O algo que no puede imaginar
#    Pila (ultimo en entrar el  primero en salir).2) Cola de prioridad  (siempre sacar el elemento más grande primero).3)  Cola  (primero en entrar el primero en salir).4) O algo que no puede imaginar
#   Entrada
#    Hay varios casos de prueba. Cada caso de prueba comienza en una linea que contiene un solo entero $n$ ($1 \leq n \leq 1000$). Cada una de las siguientes $n$ lineas es un comando de tipo de tipo1 o de tipo2. Esto quiere decir que después de ejecutar el comando de tipo2 se obtiene un entero sin error. El valor de $x$ es siempre un entero positivo no mayor a $100$. La entrada termina con un fin-de-archivo.
#    Hay varios casos de prueba. Cada caso de prueba comienza en una linea que contiene un solo entero $n$ ($1 \leq n \leq 1000$). Cada una de las siguientes $n$ lineas es un comando de tipo de tipo1 o de tipo2. Esto quiere decir que después de ejecutar el comando de tipo2 se obtiene un entero sin error. El valor de $x$ es siempre un entero positivo no mayor a $100$. La entrada termina con un fin-de-archivo.
#    Hay varios casos de prueba. Cada caso de prueba comienza en una linea que contiene un solo entero $n$ ($1 \leq n \leq 1000$). Cada una de las siguientes $n$ lineas es un comando de tipo de tipo1 o de tipo2. Esto quiere decir que después de ejecutar el comando de tipo2 se obtiene un entero sin error. El valor de $x$ es siempre un entero positivo no mayor a $100$. La entrada termina con un fin-de-archivo.
#   Salida
#    Por cada caso de prueba imprima los siguiente:stackSi la estructura de datos es definitivamente una pilaqueueSi la estructura de datos es definitivamente una colapriority queueSi la estructura de datos es definitivamente una cola de prioridadimpossibleSi no puede ser ninguna de estas estructurasnot sureSi la respuesta puede ser una o mas de las estructuras anteriores
#    Por cada caso de prueba imprima los siguiente:stackSi la estructura de datos es definitivamente una pilaqueueSi la estructura de datos es definitivamente una colapriority queueSi la estructura de datos es definitivamente una cola de prioridadimpossibleSi no puede ser ninguna de estas estructurasnot sureSi la respuesta puede ser una o mas de las estructuras anteriores
#    Por cada caso de prueba imprima los siguiente:stackSi la estructura de datos es definitivamente una pilaqueueSi la estructura de datos es definitivamente una colapriority queueSi la estructura de datos es definitivamente una cola de prioridadimpossibleSi no puede ser ninguna de estas estructurasnot sureSi la respuesta puede ser una o mas de las estructuras anteriores
#   Ejemplo Entrada
#    61 11 21 32 12 22 361 11 21 32 32 22 121 12 241 21 12 12 271 21 51 11 32 51 42 4
#   Ejemplo Salida
#    queuenot sureimpossiblestackpriority queue
#   Ayuda

while True:
    try:
        N = int(input())
        A,B,C = [],[],[]
        for i in range(N):
            x,n = map(int,input().split())
            if x==1:
                A.append(n)
            else:
                B.append(n)
        if all(a==b for a,b in zip(A,B)):
            C.append("queue")
        if all(a==b for a,b in zip(A,reversed(B))): 
            C.append("stack")
        if all(a==b for a,b in zip(sorted(A,reverse=True),sorted(B,reverse=True))): 
            C.append("priority queue")
        print(C)
    except EOFError::
        break