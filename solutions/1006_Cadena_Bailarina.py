# https://jv.umsa.bo/oj/problem.php?id=1006
#  Cadena Bailarina
#  Enviar
#  Estado
#  Descripción
#    Una cadena se llama bailarina, si y solo si, la primera letra es mayúscula y cada una de las demásletras es lo opuesto a la anterior letra (mayúscula, minúscula, mayúscula, minúscula, ..., etc.).
#    Una cadena se llama bailarina, si y solo si, la primera letra es mayúscula y cada una de las demásletras es lo opuesto a la anterior letra (mayúscula, minúscula, mayúscula, minúscula, ..., etc.).
#    Una cadena se llama bailarina, si y solo si, la primera letra es mayúscula y cada una de las demásletras es lo opuesto a la anterior letra (mayúscula, minúscula, mayúscula, minúscula, ..., etc.).
#    Por ejemplo AbCd es una cadena bailarina, la primera letra es A mayúscula, la segundaletra es b minúscula, la siguiente letra es C mayúscula y por ultimo d es minúscula.
#    Por ejemplo AbCd es una cadena bailarina, la primera letra es A mayúscula, la segundaletra es b minúscula, la siguiente letra es C mayúscula y por ultimo d es minúscula.
#    Por ejemplo AbCd es una cadena bailarina, la primera letra es A mayúscula, la segundaletra es b minúscula, la siguiente letra es C mayúscula y por ultimo d es minúscula.
#    AbCd
#    A
#    b
#    C
#    d
#    Ahora, debes construir un programa para que lea varios casos de prueba y que convierta la cadena de texto en una cadena BAILARINA.
#    Ahora, debes construir un programa para que lea varios casos de prueba y que convierta la cadena de texto en una cadena BAILARINA.
#    Ahora, debes construir un programa para que lea varios casos de prueba y que convierta la cadena de texto en una cadena BAILARINA.
#   Entrada
#    La entrada consiste en un entero T número de casos de prueba, seguido por T líneas, cada una contiene una cadena de texto, puede ser que este vacia.
#    La entrada consiste en un entero T número de casos de prueba, seguido por T líneas, cada una contiene una cadena de texto, puede ser que este vacia.
#    La entrada consiste en un entero T número de casos de prueba, seguido por T líneas, cada una contiene una cadena de texto, puede ser que este vacia.
#    T
#    T
#   Salida
#    Imprimir una línea por cada caso de prueba, que contiene la cadena bailarina resultado.
#    Imprimir una línea por cada caso de prueba, que contiene la cadena bailarina resultado.
#    Imprimir una l
#   Ejemplo Entrada
#    6oaaaabbbbaaaaRetweetedLike si resolviste el problemaAs d ffd aa sds
#   Ejemplo Salida
#    OAaAaBbBbAaAaReTwEeTeDLiKe Si ReSoLvIsTe El PrObLeMaAS d FfD aA sDs
#   Ayuda
#    El Ascci de 'a' -> 97 y de 'A' -> 65, es decir, existe 32 de diferencia en termino de valor de caracteres.

t = int(input())
for _ in range(t):
    cad = input().upper()
    nn = ""
    sw = True
    for i in range(len(cad)):
        if cad[i] == ' ':
            nn = nn + cad[i]
        else:
            if sw:
                nn = nn + cad[i]
                sw = False
            else:
                nn = nn + cad[i].lower()
                sw = True
    print(nn)