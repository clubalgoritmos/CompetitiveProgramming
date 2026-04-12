# https://jv.umsa.bo/oj/problem.php?id=1270
#  Maquina de escribir
#  Enviar
#  Estado
#  Descripción
#    Alguna vez viste una maquina de escribir, esas maquinas se dejaron de usar como hace unos 15 años, antes que las computadoras las remplacen. Tenian un mecanismo muy sencillo, tu presionas una tecla en el teclado de la maquina de escribir y un molde de la letra salta al papel y deja marcado esa letra. Algunas maquinas de escribir tenian un teclado muy duro, asi que uno tenia que presionar las teclas con mas fuerza, pero en ocasiones uno podia dañar el papel. Imagina un maquina de escribir con las letras muy afiladas las cuales podian cortar el papel en vez de imprimir en ellas.Es claro que el digito 0 dejaba un pequeño ovalo hueco en el papel. Lo mismo ocurria con algunos otros digitos: 4, 6, 9 producen un hueco, y 8 produce dos huecos. El resto de los digitos solo cortaba el papel si dejar huecos.Bob esta jugando con una vieja maquina de escribir, y se le ocurrio una idea, el quiere tomar una hoja de papel y quiere hacer exactamente $X$($0 <= X <= 17$) huecos en la hoja de papel utilizando solamente los digitos de la maquina de escribir, pero para que el juego no sea muy aburrido se puso un par de reglas, el quiere imprimir el numero con el valor mas pequeño posible y ademas quiere que el numero no tenga ceros a la izquierda.
#   Entrada
#    La entrada viene dada por varios casos de prueba, el primer numero de la entrada indica cuantos casos vienen a continuacion.Cada caso de prueba viene dado por un numero $X$ ($0 <= X <= 17$) en una linea.
#   Salida
#    Por cada caso de prueba imprime en una linea el numero que tiene X que debe ser tecleado en la maquina de escribir.
#   Ejemplo Entrada
#    30115
#   Ejemplo Salida
#    1048888888
#   Ayuda

for _ in range(int(input())):
    N = int(input())
    A = []
    while N>0:
        if N-2>=0:
            A.append(8)
            N-=2
        elif N-1>=0:
            A.append(0)
            N-=1
        else:
            break
    if A==[]:
        A=[1]
    A.sort()
    bo = False
    for i,a in enumerate(A):
        if a!=0:
            bo = True
        if not bo and a==0 and len(A)!=1:
            A[i]=4
    print(*A,sep="") 