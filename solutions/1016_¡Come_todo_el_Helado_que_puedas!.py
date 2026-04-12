# https://jv.umsa.bo/oj/problem.php?id=1016
#  ¡Come todo el Helado que puedas!
#  Enviar
#  Estado
#  Descripción
#    ¿Quién no comió helado alguna vez?, si no lo hiciste no sabes de lo que te pierdes.
#    José es un muchacho que ama los helados y siempre soñó con comer helado todo el día, por suerte él fue ahorrando dinero para poder ir al gran Palacio de los helados y comer todo el helado que pueda.
#    El palacio de los helados cuenta con infinidad de sabores como Chocolate, Vainilla, Fresa, Naranja, etc. y cada sabor viene en diferentes porciones y un precio. Por ejemplo podemos encontrar el sabor de chocolate en 3 porciones diferentes a 10Bs, 15Bs y 25Bs respectivamente.
#    José al llegar al palacio de los helados y ver los precios notó que no cuenta con suficiente dinero para poder comprar todo el helado que hay. Entonces el estará conforme con probar un helado de cada sabor.
#    Él quiere comer todos los sabores que hay y no sabe si el dinero le va a alcanzar. Así que pide tu ayuda. Él quiere gastar el máximo monto de dinero posible con la condición de probar todos los sabores que hay.
#   Entrada
#    La primera línea contiene un entero $N$, indicando el número de casos de prueba que hay. Para cada caso de prueba la primera línea tendrá 2 enteros $M$ y $C$. separados por un espacio en blanco $(1 \leq M \leq 200)$, y $(1 \leq C \leq 20)$, donde $M$ es la cantidad de dinero que pudo ahorrar José y $C$ es la cantidad de sabores que hay.
#    La primera línea contiene un entero $N$, indicando el número de casos de prueba que hay. Para cada caso de prueba la primera línea tendrá 2 enteros $M$ y $C$. separados por un espacio en blanco $(1 \leq M \leq 200)$, y $(1 \leq C \leq 20)$, donde $M$ es la cantidad de dinero que pudo ahorrar José y $C$ es la cantidad de sabores que hay.
#    La primera línea contiene un entero $N$, indicando el número de casos de prueba que hay. Para cada caso de prueba la primera línea tendrá 2 enteros $M$ y $C$. separados por un espacio en blanco $(1 \leq M \leq 200)$, y $(1 \leq C \leq 20)$, donde $M$ es la cantidad de dinero que pudo ahorrar José y $C$ es la cantidad de sabores que hay.
#    Seguidamente  existirá $C$ líneas, de cada una de estas líneas te darán un entero $K (1 \leq K \leq 20)$, indicando el número de porciones del sabor que hay, seguido por $K$ enteros indicando el precio de la porción del sabor $C_i$.
#    Seguidamente  existirá $C$ líneas, de cada una de estas líneas te darán un entero $K (1 \leq K \leq 20)$, indicando el número de porciones del sabor que hay, seguido por $K$ enteros indicando el precio de la porción del sabor $C_i$.
#    Seguidamente  existirá $C$ líneas, de cada una de estas líneas te darán un entero $K (1 \leq K \leq 20)$, indicando el número de porciones del sabor que hay, seguido por $K$ enteros indicando el precio de la porción del sabor $C_i$.
#   Salida
#    Para cada caso de prueba debe imprimir el máximo monto de dinero que José gasto en probar todos los sabores de helados (claro sin exceder este monto). Si no es posible probar todos los sabores que hay, debes imprimir “No es posible”.
#    Para cada caso de prueba debe imprimir el máximo monto de dinero que José gasto en probar todos los sabores de helados (claro sin exceder este monto). Si no es posible probar todos los sabores que hay, debes imprimir “No es posible”.
#    Para cada caso de prueba debe imprimir el máximo monto de dinero que José gasto en probar todos los sabores de helados (claro sin exceder este monto). Si no es posible probar todos los sabores que hay, debes imprimir “No es posible”.
#   Ejemplo Entrada
#    3100 43 8 6 42 5 104 1 3 3 74 50 14 23 820 33 4 6 82 5 104 1 3 5 55 33 6 4 82 10 64 7 3 1 7
#   Ejemplo Salida
#    7519No es posible
#   Ayuda
#    2da div. 2012 UMSA

for _ in range(int(input())):
    M, C = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(C)]
    dp = [0] * (M + 1)
    for i in range(C):
        for j in range(s[i][0], M + 1):
            dp[j] = max(dp[j], dp[j - s[i][0]] + s[i][1])
    print("No es posible" if dp[M] == 0 else dp[M])