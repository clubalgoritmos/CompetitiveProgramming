# https://jv.umsa.bo/oj/problem.php?id=1279
#  Cifrado Cesar
#  Enviar
#  Estado
#  Descripción
#    Escriba un programa que codifique mensajes con el cifrado de Cesar. Este cifrado lo utilizo Julio Cesar para comunicarse con sus generales.
#    Dada una constante $K$, cada letra del mensaje original se remplaza por una letra que esta alfabeticamente $K$ posiciones a la derecha , en forma circular si pasa la ultima letra del alfabeto.
#    Por ejemplo si $K=5$ debemos cambiar $a$ por $f$, $b$ por $g$, ... y $z$ por $e$.
#   Entrada
#    La entrada consiste de varios casos de prueba. Cada caso de prueba comienza con un numero natural $k>0$, seguido de una cadena $1 \leq |cad| \leq 50$ de solo letras minúsculas. Existe un separador de palabras pero no un espacio. El separador puede se un caracter que no sea una letra minúscula.
#   Salida
#    Para cada caso de prueba escriba una linea con el texto cifrado en mayúsculas. Remplace los guiones bajos por espacio. Deje los caracteres de separación de palabras sin cambio.
#   Ejemplo Entrada
#    1 i_am_an_example22 veni,vidi,vinci26000031 yzznhzzn-eznczo-wjiz-yjnzaz_ypqzhv-zidozhjnn
#   Ejemplo Salida
#    J BN BO FYBNQMFRAJE,REZE,REJYEDEESMEES-JESHET-BONE-DOSEFE DUVEMA-ENITEMOSS
#   Ayuda
#    $OK$

while True:
    try:
        k, S = input().split()
        k = int(k)
        for s in S:
            if s.isalpha():
                print(chr((ord(s)-97+k)%26+65), end="")
            elif s != "_":
                print(s, end="")
            else:
                print(" ", end="")
        print()
    except EOFError:
        break