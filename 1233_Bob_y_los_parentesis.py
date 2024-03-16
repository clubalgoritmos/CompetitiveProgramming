# https://jv.umsa.bo/oj/problem.php?id=1233
#  Bob y los parentesis
#  Enviar
#  Estado
#  Descripción
#    Bob es un estudiante de la materia "Introducción a la Programación" y hoy es su primera clase. Y el docente le esta enseñando a programar en Java. Y el docente les explica...
#    Cada vez que abren un parentesis '(' o un corchete '[' deben tener sus respectivos parentesis/corchetes de cierre o su programa no compilara...bla bla bla bla bla bla...
#    Pero Bob ya sabia todo eso así que en vez de escuchar las explicaciones del docente decide ponerse a verificar su ejercicios. Para hacer mas facil su trabajo decide usar su editor de texto favorito, el cual tiene un comando especial(mágico) con el cual puede eliminar todos los caracteres que no sean parentesis, corchetes o espacios del archivo abierto. Luego Bob debe verificar solamente una linea por ejercicio.
#    ¿Puedes ayudar a Bob a verificar si sus ejercicios contienen una estructura correcta de parentesis y corchetes?
#   Entrada
#    La primera linea de entrada contendra un numero $N$ ($1 \leq N \leq 2000$) que representa la cantidad de archivos que debe verificar Bob.
#    Cada una de las siguientes $N$ lineas conteandra una linea de hasta $1000$ caracteres '$($', '$)$', '$[$', '$]$' o ' '(espacio) que representa un archivo en el cual Bob aplico el comando magico con su editor.
#   Salida
#    Por cada linea que representa un archivo que Bob debe verificar imprimir una linea con la palabra "Yes" (sin comilla) si el archivo contiene una estructura correcta de parentesis y/o corechetes, y "No" (sin comillas) en caso contrario.
#   Ejemplo Entrada
#    13()[()]([)][[]](([()])))(()()())  ]][]([()[]()])()[ [ ((][]([])([() ] [)( ]
#   Ejemplo Salida
#    YesYesNoYesNoYesNoYesNoYesNoNoNo
#   Ayuda
#    Atención: La entrada podria contener espacios extra en cualquier lugar del archivo de entrada.

for _ in range(int(input())):
    S = input().strip()
    vec = []
    for i, si in enumerate(S):
        if si in {"(", "["}:
            vec.append(si)
        elif vec and ((vec[-1] == "(" and si == ")") or (vec[-1] == "[" and si == "]")):
            vec.pop()
        else:
            vec.append(si)
    print("Yes" if not vec else "No")