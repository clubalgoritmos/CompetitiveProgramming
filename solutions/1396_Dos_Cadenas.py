# https://jv.umsa.bo/oj/problem.php?id=1396
## https://jv.umsa.bo/oj/problem.php?id=1396
#  Dos Cadenas
#  Enviar
#  Estado
#  Descripción
#    Dos cadenas se dicen completas si después de concatenadas contienen las 26 letras del alfabeto eningles. Por ejemplo, abcdefghi y jklmnopqrstuvwxyz se llamaran completas porque juntastienen todas los caracteres de desde la 'a' a la 'z'.Nos darán dos conjuntos A y B conteniendo cadenas con tamaños n y m respectivamente. Sequiere hallar el numero pares de cadenas que forman cadenas completas.
#   Entrada
#    La entrada consiste de múltiples pares de cadenas. Dos cadenas vienen en dos lineas.Las cadenas solo contienen letras del alfabeto ingles en minúsculas.La entrada termina termina cuando no hay más datos.
#   Salida
#    En la salida escriba la palabra "Completa" si tomando ambas cadenas contiene las 26 letras del alfabeto ingles, al menos una vez.En otros caso escriba la palabra "Incompleta"
#   Ejemplo Entrada
#    abcdefghijklmnopqrstuvwxyzabcxyzzzzzzzzzzzzzz
#   Ejemplo Salida
#    CorrectoIncorrecto
#   Ayuda
while True:
    try:
        S = input()+input()
        if all(si in S for si in "abcdefghijklmnopqrstuvwxyz"):
            print("Correcto")
        else:
            print("Incorrecto")
    except EOFError:
        break