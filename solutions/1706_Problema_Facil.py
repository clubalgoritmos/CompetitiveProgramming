# https://jv.umsa.bo/oj/problem.php?id=1706
#  Problema Facil?
#  Enviar
#  Estado
#  Descripción
#    Al preparar un Examen, los coordinadores del Juez hacen todo lo posible para que el primer problema sea lo más fácil posible. Esta vez, el coordinador había elegido algún problema y preguntó a n personas sobre sus opiniones. Cada persona respondió si este problema es fácil o difícil.
#    Si al menos una de estas n personas ha respondido que el problema es difícil, el coordinador decide cambiar el problema. Para las respuestas dadas, verifique si el problema es lo suficientemente fácil.
#   Entrada
#    El problema tendra varios casos de prueba.
#    Para cada caso la primera línea contiene un solo entero n (1≤n≤100): el número de personas a las que se les pidió que expresaran sus opiniones.
#    La segunda línea contiene n enteros, cada entero es 0 o 1. Si i-th integer es 0, entonces i-th persona piensa que el problema es fácil; si es 1, entonces i-th persona piensa que el problema es difícil.
#   Salida
#    Imprima una palabra: "EASY" si el problema es fácil de acuerdo con todas las respuestas, o "HARD" si hay al menos una persona que piensa que el problema es difícil.
#   Ejemplo Entrada
#    30 0 110
#   Ejemplo Salida
#    HARDEASY
#   Ayuda

"""problema facil?"""
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        p = input()
        if(p.__contains__("1")):
            print("HARD")
        else:
            print("EASY")