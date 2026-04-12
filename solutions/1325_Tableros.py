# https://jv.umsa.bo/oj/problem.php?id=1325
#  Tableros
#  Enviar
#  Estado
#  Descripción
#    Un patrón de tablero de ajedrez es un tablero que satisface las siguientes condiciones:Tiene una forma rectangularContiene punto y la letra mayúscula $X$.Ninguno de los dos símbolos adyacentes, tanto horizontales y verticales son igualesEl símbolo de la esquina inferior derecha es un punto.
#   Entrada
#    En la entrada existen varios casos de prueba. Cada caso de prueba consiste de dos enteros separados por un espacio. Estos estarán en el rango de $1$ y $50$ inclusive. El primer entero representa el número de filas del tablero a construir y el segundo el número de columnas. La entrada termina cuando no hay mas casos de prueba.
#   Salida
#    La salida consiste en el tablero formado. El tablero se imprime fila por fila. Al final del tablero se imprime una fila con $10$ guiones ($-$).
#   Ejemplo Entrada
#    8 81 201 12 2
#   Ejemplo Salida
#    .X.X.X.XX.X.X.X..X.X.X.XX.X.X.X..X.X.X.XX.X.X.X..X.X.X.XX.X.X.X.----------X.X.X.X.X.X.X.X.X.X.----------.----------.XX.----------
#   Ayuda
while True:
    try:
        x,y = map(int, input().split())
        for i in range(x):
            for j in range(y):
                if (i+j)%2!=0:
                    print("X", end="")
                else:
                    print(".", end="")
            print()
        print("-"*10)
    except EOFError:
        break