# https://jv.umsa.bo/oj/problem.php?id=1085
## https://jv.umsa.bo/oj/problem.php?id=1085
#  Ordenando Panqueques
#  Enviar
#  Estado
#  Descripción
#    Cocinar panqueques en una sartén es bastante complicado porque sin importar cuanto se esmere todos tendrán un diámetro diferente. Para la presentación de la pila usted los puede ordenar por tamaño de tal manera que cada panqueque es mas pequeño de los que están mas abajo. El tamaño esta dado por el diámetro.  La pila se ordena por una secuencia de volteos. Un volteo consiste en insertar una espátula entre dos panqueques y volteando todos los panqueques en la espátula  (colocando en orden reverso la subpila). Un volteo se especifica indicando la posición del panqueque en la base de la subpila a ser voleado. El panqueque de la base tiene la posición 1 y el de encima $n$.  La pila se especifica dando el diámetro de cada panqueque en orden en que aparecen. Por ejemplo considere las tres pilas de panqueques en el cual 8 es el panqueque encima de la pila de la izquierda
#    La pila de la izquierda puede ser transformada a la pila del medio por $volteo(3)$. La del medio puede transformarse en la de la derecha con $volteo(1)$. \section{Entrada} La entrada consiste en secuencias de pilas de panqueques. Cada pila consiste de 1  a 20 panqueques y cada panqueque tendrá un diámetro entero entre 1 y 100. la entrada se termina con un fin de archivo. Cada pila esta dada en una fila con el panqueque de arriba primero y el de la base al final. Todos ellos separados por un espacio.
#   Entrada
#    La entrada consiste en secuencias de pilas de panqueques. Cada pila consiste de 1 a 20 panqueques y cada panqueque tendrá un diámetro entero entre 1 y 100.la entrada se termina con un fin de archivo. Cada pila esta dada en una fila con el panquequede arriba primero y el de la base al final. Todos ellos separados por un espacio.
#   Salida
#    Para cada pila de panqueques su programa debe imprimir la pila original en una línea seguido de una secuencia de volteos que ordena la pila de panqueques de tal forma que el panqueque mas grande este abajo y el mas pequeño arriba.la secuencia de volteos debe terminar con un 0 indicando que no se requieren mas volteos.Cuando la pila esta ordenada no se deben realizar mas volteos
#   Ejemplo Entrada
#    1 2 3 4 55 4 3 2 15 1 2 3 4
#   Ejemplo Salida
#    1 2 3 4 505 4 3 2 11 05 1 2 3 41 2 0
#   Ayuda

while True:
    try:
        A = list(map(int,input().split()))
        print(*A)
        flips = []
        for j in range(len(A)-1, -1, -1):
            max_index = A.index(max(A[:j+1]))
            if max_index != j:
                if max_index != 0:
                    A[:max_index+1] = reversed(A[:max_index+1])
                    flips.append(len(A) - max_index)
                A[:j+1] = reversed(A[:j+1])
                flips.append(len(A) - j)
        flips.append(0)
        print(" ".join(map(str, flips)))
    except EOFError:
        break