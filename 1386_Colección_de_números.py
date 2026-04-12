# https://jv.umsa.bo/oj/problem.php?id=1386
#  Colección de números
#  Enviar
#  Estado
#  Descripción
#    S x : guarda una copia de un numero x.A : Imprime el número más grande.R : extrae el numero más grande.I x : incrementa el numero más grande en x.D x : decrementa el numero más grande en x.T : termina la entrada.
#   Entrada
#    La entrada consiste de muchas operaciones.
#   Salida
#    Muestre los resultados al procesar la secuencia de instrucciones.
#   Ejemplo Entrada
#    S 10AI 10AD 5ARRS 100D 20 S 20S 20AI 5AT
#   Ejemplo Salida
#    102015Error8085
#   Ayuda

memo = []

def sumar(x):
    memo[memo.index(max(memo))] += x

def restar(x):
    memo[memo.index(max(memo))] -= x

dicts = {
    "S": lambda x: memo.append(int(x)),
    "A": lambda: print(max(memo)),
    "R": lambda: memo.pop(memo.index(max(memo))),
    "I": lambda x: sumar(int(x)),
    "D": lambda x: restar(int(x)),
}
while True:
    try:
        entry = tuple(input().split())

        if entry[0]=="T":
            break
        if len(entry)>1:
            dicts[entry[0]](entry[1])
        else:
            dicts[entry[0]]()         
    except Exception as e:
        print("Error")
        pass