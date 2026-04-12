# https://jv.umsa.bo/oj/problem.php?id=1348
## https://jv.umsa.bo/oj/problem.php?id=1348
#  Esperanto
#  Enviar
#  Estado
#  Descripción
#    Los números son mucho más fáciles de escribir en esperanto que en español. Los números del 1 al 10 se detallan como sigue: $unu$, $du$, $tri$, $kvar$, $Kvin$, $ses$, $Sep$, $OK$, $Nau$, $dek$. Números del 11 al 19 se escriben: $dek \; unu$, $dek \; du$, ..., $dek \; Nau$, un $dek$ seguido de un solo espacio y el nombre del último dígito. Números 20 al 29 se escriben: $dudek$, $dudek \; unu$, $dudek \; du$, ..., $dudek \; Nau$. Del mismo modo, 30 es $tridek$, ..., 90 es $Naudek$. Sólo se unen el número de decena y $dek$. No hay excepciones como $doce$ o $quince$ en español.
#   Entrada
#   Salida
#    Por cada caso de prueba en la entrada escriba una línea con el nombre en esperanto.
#   Ejemplo Entrada
#    1 901177
#   Ejemplo Salida
#    unuNaudekdek unuSepdek Sep
#   Ayuda

NUM = ["","unu", "du", "tri", "kvar", "Kvin", "ses", "Sep", "OK", "Nau", "dek"]

while True:
    try:
        S = input().strip()
        esperanto_nums = [(NUM[int(si)] if not (len(S)-1-i==1 and si=="1") else "") + ("dek" if len(S)-1-i>=1 else "") for i, si in enumerate(S)]
        print(" ".join(num for num in esperanto_nums if num))
    except EOFError:
        break