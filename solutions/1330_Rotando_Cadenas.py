# https://jv.umsa.bo/oj/problem.php?id=1330
#  Rotando Cadenas
#  Enviar
#  Estado
#  Descripción
#    Definimos una rotación a la derecha de una cadena S como tomar el ultimo caracter de la cadena y llevarlo al inicio.Por ejemplo dada la cadena "qwerty" una rotación a la derecha dara la cadena "yqwert", dos rotaciones a la derecha dara "tyqwer", tres rotaciones a la derecha "rtyqwe", etc.
#    Definimos una rotación a la derecha de una cadena S como tomar el ultimo caracter de la cadena y llevarlo al inicio.Por ejemplo dada la cadena "qwerty" una rotación a la derecha dara la cadena "yqwert", dos rotaciones a la derecha dara "tyqwer", tres rotaciones a la derecha "rtyqwe", etc.
#    Definimos una rotación a la derecha de una cadena S como tomar el ultimo caracter de la cadena y llevarlo al inicio.Por ejemplo dada la cadena "qwerty" una rotación a la derecha dara la cadena "yqwert", dos rotaciones a la derecha dara "tyqwer", tres rotaciones a la derecha "rtyqwe", etc.
#    qwerty
#    yqwert
#    tyqwer
#    rtyqwe
#   Entrada
#    La cadena S y un numero entero R que representa el numero de rotaciones a la derecha a realizar sobre la cadena S. S no tendra espacios.(1 <= Longitud de la cadena S <= 40, 0 <= R <= Longitud de S)
#    La cadena S y un numero entero R que representa el numero de rotaciones a la derecha a realizar sobre la cadena S. S no tendra espacios.(1 <= Longitud de la cadena S <= 40, 0 <= R <= Longitud de S)
#    La cadena S y un numero entero R que representa el numero de rotaciones a la derecha a realizar sobre la cadena S. S no tendra espacios.(1 <= Longitud de la cadena S <= 40, 0 <= R <= Longitud de S)
#    S
#    R
#    S
#    S
#    1 <= Longitud de la cadena S <= 40
#    0 <= R <= Longitud de S
#   Salida
#    La cadena S despues de realizar R rotaciones a la derecha.
#    La cadena S despues de realizar R rotaciones a la derecha.
#    La cadena S despues de realizar R rotaciones a la derecha.
#   Ejemplo Entrada
#    SuperNintendoChalmers 8
#   Ejemplo Salida
#    ChalmersSuperNintendo
#   Ayuda
#    se sugiere usar un vector de caracteres para su facil rotacion

S,N = input().split()
N = int(N) % len(S)
if N == 0:
    print(S)
else:
    print(S[-N:] + S[:-N])