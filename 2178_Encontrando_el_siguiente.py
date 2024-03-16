# https://jv.umsa.bo/oj/problem.php?id=2178
#  Encontrando el siguiente
#  Enviar
#  Estado
#  Descripción
#    En la clase nos han dado la siguiente lista de sucesiones de números contiguos:
#    Fíjese que el resultado es la suma de los números en la secuencia y la suma anterior siempre figura en el resultado.  Lo que se quiere conocer es cual es el siguiente resultado de la suma de consecutivos. En el problema se proporciona el número $n$ y se trata de conocer cual es el resultado de la sucesión, por ejemplo:
#    como se puede ver en la sucesión.
#   Entrada
#    La primera línea de cada caso de prueba contiene un número $T$ ($1 \leq T \leq 100$) que indica la cantidad de números a ser evaluados.
#    Las siquientes $T$  lineas tendrań un número $n$ ($1 \leq n \leq 100$).
#   Salida
#    Por cada número $n$ imprima los dos números que corresponde de la separados por un símbolo de suma como se muestra en el ejemplo.
#   Ejemplo Entrada
#    41234
#   Ejemplo Salida
#    11+88+2727+64
#   Ayuda

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        continue
    print(f"{(n-1)**3}+{n**3}")
