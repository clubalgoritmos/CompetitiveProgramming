# https://jv.umsa.bo/oj/problem.php?id=1912
## https://jv.umsa.bo/oj/problem.php?id=1912
#  Lotes 1
#  Enviar
#  Estado
#  Descripción
#    Dado un lote de $n$ numeros, determinar cuantos números pares e impares hay en el lote.
#    Dado un lote de $n$ numeros, determinar cuantos números pares e impares hay en el lote.
#    Dado un lote de $n$ numeros, determinar cuantos números pares e impares hay en el lote.
#   Entrada
#    La primera linea contiene un número $n$ ($1 \leq n \leq 1000$), el cual indica cuantos números leer.
#    La primera linea contiene un número $n$ ($1 \leq n \leq 1000$), el cual indica cuantos números leer.
#    La primera linea contiene un número $n$ ($1 \leq n \leq 1000$), el cual indica cuantos números leer.
#    Las siguientes $n$ lineas contienen un $n$-ésimo número por linea. ($1 \leq n_{i} \leq 1000$)
#    Las siguientes $n$ lineas contienen un $n$-ésimo número por linea. ($1 \leq n_{i} \leq 1000$)
#    Las siguientes $n$ lineas contienen un $n$-ésimo número por linea. ($1 \leq n_{i} \leq 1000$)
#   Salida
#    Imprima cuantos números pares e impares existen en el lote.
#    Imprima cuantos números pares e impares existen en el lote.
#    Imprima cuantos números pares e impares existen en el lote.
#   Ejemplo Entrada
#    512345
#   Ejemplo Salida
#    Pares: 2Impares: 3
#   Ayuda

N = int(input())
pares, impares = 0,0
for _ in range(N):
    n = int(input())
    if n%2==0:
        pares += 1
        continue
    impares += 1
print(f"Pares: {pares}\nImpares: {impares}")