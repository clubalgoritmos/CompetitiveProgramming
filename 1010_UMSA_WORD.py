# https://jv.umsa.bo/oj/problem.php?id=1010
#  UMSA WORD
#  Enviar
#  Estado
#  Descripción
#    La organización de la ICPC BOLIVIA hizo hacer letras grandes, para usarlas como publicidad en el evento.
#    Mientras transportaban el paquete que almacenaba las letras este se rompió y dejo caer las letras, al caer las letras varias de estas se perdieron.  Así que ellos no están seguros si con las letras restantes podrán armar las palabras que ellos quieren.
#    Por ejemplo si tenemos las letras U, S, M, A, C, D, I, C, P, C y queremos armar la palabra ICPC UMSA, notaremos claramente que es posible armarla. En cambio si tuviéramos las letras U, M, S, D, G, I, I, C, P no será posible armar la palabra ICPC UMSA pues faltaría la letra “A”.
#    Los organizadores piden tu ayuda. Ellos te darán las letras disponibles y quieren saber si es posible armar la palabra UMSA ICPC.
#   Entrada
#   Salida
#   Ejemplo Entrada
#    3UMSAICPCICPCUMSAICPCUMSHJK
#   Ejemplo Salida
#    ES POSIBLEES POSIBLENO ES POSIBLE
#   Ayuda

S0 = {
    "U":1,
    "M":1,
    "S":1,
    "A":1,
    "I":1,
    "C":2,
    "P":1
}
for _ in range(int(input())):
    S = input()
    for k,v in S0.items():
        if S.count(k)<v:
            print("NO ES POSIBLE")
            break
    else:
        print("ES POSIBLE")
    
