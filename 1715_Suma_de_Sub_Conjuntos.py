# https://jv.umsa.bo/oj/problem.php?cid=2820&pid=1
## https://jv.umsa.bo/oj/problem.php?id=1715
#  Suma de Sub Conjuntos
#  Enviar
#  Estado
#  Descripción
#    Dado un conjunto de números enteros positivos y negativos, nos piden hallar todos los sub conjuntos que den una suma dada. Por ejemplo si tenemos el conjunto {-2,1,3} todos los subconjuntos que existen dan una suma como se muestra:
#    {} suma=0{-2} suma=-2{1} suma=1{3} suma=3{-2,1} suma=-1{-2,3\} suma=1{1,3} suma=4{-2,1,3} suma=2Nos dan la suma que buscamos y la lista de números del conjunto. En el ejemplo dado si se quiere saber cuantos subconjuntos suman 1, la respuesta seria 2.
#   Entrada
#    La entrada consiste en varios casos de prueba. Cada caso de prueba consiste de dos lineas, la primera tiene la suma buscada ($0 \leq s \leq 10000$) y el numero de elementos del vector ($1 \leq n \leq 10$), separados por un espacio. La segunda linea contiene los n elementos del vector separados por un espacio.
#   Salida
#    Por cada caso de prueba escriba una linea con el numero de subconjuntos que dan la suma pedida.
#   Ejemplo Entrada
#    1 3-2 1 35 51 2 3 4 5
#   Ejemplo Salida
#    23
#   Ayuda

# Ejecuta el código hasta que se encuentre un error de fin de archivo (EOFError)
while True:
    try:
        # Lee el número objetivo 's' y el número de elementos 'n'
        s, n = map(int,input().split())
        # Lee los 'n' elementos
        A = list(map(int,input().split()))
        # Inicializa el contador de subconjuntos que suman 's'
        c=0
        # Genera todos los posibles subconjuntos de 'A'
        for i in range(1,1<<n):
            # Inicializa la suma del subconjunto actual
            suma=0
            # Verifica cada bit de 'i'
            for j in range(n):
                # Si el bit 'j' de 'i' está encendido, añade 'A[j]' a 'suma'
                if i&(1<<j):
                    suma+=A[j]
            # Si la suma del subconjunto actual es igual a 's', incrementa el contador
            if suma==s:
                c+=1
        # Imprime el número de subconjuntos que suman 's'
        print(c)
    # Si se encuentra un error de fin de archivo (EOFError), termina el programa
    except EOFError:
        break