# https://jv.umsa.bo/oj/problem.php?cid=2575&pid=8
#  Bob y su ganado
#  Estado
#  Descripción
#    El granjero Bob ha construido un nuevo granero largo, con $N$ puestos. Los puestos se ubican en línea recta en las posiciones $x_{1}, x_{2},..., x_{N}$.
#    El granjero Bob ha construido un nuevo granero largo, con $N$ puestos. Los puestos se ubican en línea recta en las posiciones $x_{1}, x_{2},..., x_{N}$.
#    El granjero Bob ha construido un nuevo granero largo, con $N$ puestos. Los puestos se ubican en línea recta en las posiciones $x_{1}, x_{2},..., x_{N}$.
#    A sus $C$ vacas no les gusta este diseño de establo y se vuelven agresivas entre sí una vez que las colocan en el establo. Para evitar que las vacas se lastimen entre sí, el granjero Bob quiere asignar las vacas a los establos, de modo que la distancia mínima entre dos de ellas sea lo más grande posible. ¿Cuál es la distancia mínima más grande?
#    A sus $C$ vacas no les gusta este diseño de establo y se vuelven agresivas entre sí una vez que las colocan en el establo. Para evitar que las vacas se lastimen entre sí, el granjero Bob quiere asignar las vacas a los establos, de modo que la distancia mínima entre dos de ellas sea lo más grande posible. ¿Cuál es la distancia mínima más grande?
#    A sus $C$ vacas no les gusta este diseño de establo y se vuelven agresivas entre sí una vez que las colocan en el establo. Para evitar que las vacas se lastimen entre sí, el granjero Bob quiere asignar las vacas a los establos, de modo que la distancia mínima entre dos de ellas sea lo más grande posible. ¿Cuál es la distancia mínima más grande?
#   Entrada
#    La entrada cosiste en un entero $t$ ($1 \leq t \leq 10$) - el número de casos de prueba, luego sigue $t$ casos de prueba:
#    La entrada cosiste en un entero $t$ ($1 \leq t \leq 10$) - el número de casos de prueba, luego sigue $t$ casos de prueba:
#    La entrada cosiste en un entero $t$ ($1 \leq t \leq 10$) - el número de casos de prueba, luego sigue $t$ casos de prueba:
#    Línea 1: Dos enteros separados por espacios: $N$ que indica la cantidad de puestos en la granja y $C$ que indica la cantidad de vacas ($2 \leq C \leq  N \leq 10^{5}$) .
#    Línea 2: $N$ enteros $x_{1}, x_{2},..., x_{N}$ ($0 \leq x_{i} \leq 10^{9}$), que indican las posiciones de cada puesto.
#   Salida
#    Para cada caso de prueba, genere un número entero: la distancia mínima más grande entre cada par de vacas.
#   Ejemplo Entrada
#    25 31284910 4141021152618313650
#   Ejemplo Salida
#    314
#   Ayuda

for _ in range(int(input())):
    N,C = map(int,input().split())
    ubica = []
    for _ in range(N):
        ubica.append(int(input()))

    def check(mid):
        cows = 1sd
        pos = ubica[0]
        for i in range(1, N):
            if ubica[i] - pos >= mid:
                pos = ubica[i]
                cows += 1
                if cows == C:
                    return True
        return False

    ubica.sort()
    ini = 1
    fin = ubica[-1] - ubica[0]
    res = 0

    while ini <= fin:
        mid = (ini + fin) // 2
        if check(mid):
            res = mid
            ini = mid + 1
        else:
            fin = mid - 1

    print(res)