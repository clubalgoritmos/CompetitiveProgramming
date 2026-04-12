# https://jv.umsa.bo/oj/problem.php?id=1997
#  Escribir en el Teclado
#  Enviar
#  Estado
#  Descripción
#    Hoy te haz comprado una nueva televisión, y es smart!!.Trae un teclado que aparece en la pantalla cuando quieres buscar algo. El diagrama del mismo es como sigue:a b c d e f g h i jk l m n o p q r s tu v w x y z esp enter bksCada vez que accedes al teclado estas ubicado en la letra a. Para moverte a otra letra solo tienes disponibles las flechas izquierda, derecha, arriba y abajo.Para simplicidad solo se tomarán en cuenta las letras minúsculas del alfabeto. Dada una cadena que contiene letras minúsculas y espacio se quiere estimar el mínimo numero de movimientos que se debe hacer para escribir esta palabra.Por ejemplo para escribir "solo inf" para ir a la "s" se requieren 10 movimientos. De la "s" a la "o" 4, de la "o" a la "l" 3, etc. El espacio esta debajo de la "q" y se termina con un "enter" que esta debajo de la "r".
#   Entrada
#    La comienza con un numero entero que representa el  numera de cadenas en el caso de prueba. Cada cadena viene en una línea  y contiene como máximo 1000 caracteres minúsculas y espacio. Considere  que aún cuando no se puso un "enter" al final de la cadena debe  introducir uno.
#   Salida
#    Por cada cadena escriba el mínimo numero de movimientos que hay que hacer para escribir esta cadena.
#   Ejemplo Entrada
#    3solo infinfaaa
#   Ejemplo Salida
#    39219
#   Ayuda

M = [["a","b","c","d","e","f","g","h","i","j"],
["k","l","m","n","o","p","q","r","s","t"],
["u","v","w","x","y","z"," ","*","bks"]]

def encuentra_x_desde_ij(x,i,j):
    for i1 in range(3):
        for j1 in range(10):
            if M[i1][j1]==x:
                return abs(i1-i)+abs(j1-j),i1,j1

for _ in range(int(input())):
    S = input()+"*"
    i,j=0,0
    su=0
    for s in S:
        s,i,j=encuentra_x_desde_ij(s,i,j)
        su+=s
    print(su)        