# https://jv.umsa.bo/oj/problem.php?id=1570
#  Criptografía
#  Enviar
#  Estado
#  Descripción
#    Algunas operaciones criptográficas requieren de la exponenciación modular.Es decir, dado enteros $b, e, m$ calcular $b^e$ mod $m$. En este problema te pedimos que escribas un algoritmo eficiente para calcular dicha operación.
#   Entrada
#    En la primera línea de entrada se te proporcionara un entero $T$, el número de casos de prueba.Seguidamente deberás leer $T$ líneas, cada linea contendrá tres enteros positivos$b, e$ y $m$. Puedes asumir que $1 < b, m < 2^{15}$, y $0 < e < 2^{31}$.
#   Salida
#    La salida consiste de una línea por cada caso de prueba en la cual deberás imprimir el resultado de la operación descrita arriba.
#   Ejemplo Entrada
#    22 3 52 2147483647 13
#   Ejemplo Salida
#    311
#   Ayuda
#    Divide y Vencerás

def fast_modular_exponentiation(b, e, m):
    res = 1
    b %= m

    while e > 0:
        if e & 1:  # Si el bit más a la derecha de e es 1
            res = (res * b) % m
        b = (b * b) % m
        e >>= 1  # Desplaza e un bit a la derecha

    return res

for _ in range(int(input())):
    b,e,m = map(int, input().split())
    print(fast_modular_exponentiation(b, e, m))
