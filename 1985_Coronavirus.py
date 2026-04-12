# https://jv.umsa.bo/oj/problem.php?id=1985
#  Coronavirus
#  Enviar
#  Estado
#  Descripción
#    Debido a la lucha contra el enemigo invisible (COVID-19), Valeria a organizado a un grupo de n personas para la fumigación de las calles de su zona. Ella a numerado a las personas de $1$ a $n$, ($a$1, $a$2, $a$3,…, $a$n). Valeria conoce la cantidad de hipoclorito sódico que tiene cada persona en su mochila pulverizadora, la persona i tiene ai de hipoclorito sódico en su mochila pulverizadora (obviamente esta cantidad está definida en centímetros cúbicos, pero esto no viene al caso).
#    Debido a la lucha contra el enemigo invisible (COVID-19), Valeria a organizado a un grupo de n personas para la fumigación de las calles de su zona. Ella a numerado a las personas de $1$ a $n$, ($a$1, $a$2, $a$3,…, $a$n). Valeria conoce la cantidad de hipoclorito sódico que tiene cada persona en su mochila pulverizadora, la persona i tiene ai de hipoclorito sódico en su mochila pulverizadora (obviamente esta cantidad está definida en centímetros cúbicos, pero esto no viene al caso).
#    Debido a la lucha contra el enemigo invisible (COVID-19), Valeria a organizado a un grupo de n personas para la fumigación de las calles de su zona. Ella a numerado a las personas de $1$ a $n$, ($a$1, $a$2, $a$3,…, $a$n). Valeria conoce la cantidad de hipoclorito sódico que tiene cada persona en su mochila pulverizadora, la persona i tiene ai de hipoclorito sódico en su mochila pulverizadora (obviamente esta cantidad está definida en centímetros cúbicos, pero esto no viene al caso).
#    Valeria desea dividir a las $n$ personas en dos equipos. Cada equipo debe tener al menos una persona, y cada persona debe estar exactamente en un equipo.
#    Valeria desea dividir a las $n$ personas en dos equipos. Cada equipo debe tener al menos una persona, y cada persona debe estar exactamente en un equipo.
#    Valeria desea dividir a las $n$ personas en dos equipos. Cada equipo debe tener al menos una persona, y cada persona debe estar exactamente en un equipo.
#    Valeria quiere que la persona que tiene mayor cantidad de hipoclorito sódico del primer equipo difiera lo menos posible con la persona que tiene la menor cantidad de hipoclorito sódico del segundo equipo. Formalmente, ella desea dividir a las personas en dos equipos $A$ y $B$ para que el valor |$max$ ($A$) − $min$($B$)| sea lo más pequeño posible, donde $max$($A$) es la cantidad máxima de hipoclorito sódico de una persona del equipo $A$, y $min$($B$) es la cantidad mínima de hipoclorito sódico de la persona del equipo $B$.
#    Valeria quiere que la persona que tiene mayor cantidad de hipoclorito sódico del primer equipo difiera lo menos posible con la persona que tiene la menor cantidad de hipoclorito sódico del segundo equipo. Formalmente, ella desea dividir a las personas en dos equipos $A$ y $B$ para que el valor |$max$ ($A$) − $min$($B$)| sea lo más pequeño posible, donde $max$($A$) es la cantidad máxima de hipoclorito sódico de una persona del equipo $A$, y $min$($B$) es la cantidad mínima de hipoclorito sódico de la persona del equipo $B$.
#    Valeria quiere que la persona que tiene mayor cantidad de hipoclorito sódico del primer equipo difiera lo menos posible con la persona que tiene la menor cantidad de hipoclorito sódico del segundo equipo. Formalmente, ella desea dividir a las personas en dos equipos $A$ y $B$ para que el valor |$max$ ($A$) − $min$($B$)| sea lo más pequeño posible, donde $max$($A$) es la cantidad máxima de hipoclorito sódico de una persona del equipo $A$, y $min$($B$) es la cantidad mínima de hipoclorito sódico de la persona del equipo $B$.
#    Por ejemplo, si $n$ = $5$ y la cantidad de cada persona es $a$ = [$3$,$1$,$2$,$6$,$4$], una de las posibles divisiones que hará Valeria es:
#    Por ejemplo, si $n$ = $5$ y la cantidad de cada persona es $a$ = [$3$,$1$,$2$,$6$,$4$], una de las posibles divisiones que hará Valeria es:
#    Por ejemplo, si $n$ = $5$ y la cantidad de cada persona es $a$ = [$3$,$1$,$2$,$6$,$4$], una de las posibles divisiones que hará Valeria es:
#    •Primer equipo: $A$ = [$1$,$2$,$3$]•Segundo equipo: $B$ = [$4$,$6$]
#    •Primer equipo: $A$ = [$1$,$2$,$3$]•Segundo equipo: $B$ = [$4$,$6$]
#    •Primer equipo: $A$ = [$1$,$2$,$3$]•Segundo equipo: $B$ = [$4$,$6$]
#    En este caso, el valor |$max$ ($A$) − $min$ ($B$)| será igual a |$3$−$4$| = $1$. Este ejemplo ilustra una de las formas de división óptima en dos equipos.
#    En este caso, el valor |$max$ ($A$) − $min$ ($B$)| será igual a |$3$−$4$| = $1$. Este ejemplo ilustra una de las formas de división óptima en dos equipos.
#    En este caso, el valor |$max$ ($A$) − $min$ ($B$)| será igual a |$3$−$4$| = $1$. Este ejemplo ilustra una de las formas de división óptima en dos equipos.
#    Ayuda a Valeria a encontrar el valor mínimo |$max$ ($A$) − $min$ ($B$)|.
#    Ayuda a Valeria a encontrar el valor mínimo |$max$ ($A$) − $min$ ($B$)|.
#    Ayuda a Valeria a encontrar el valor mínimo |$max$ ($A$) − $min$ ($B$)|.
#   Entrada
#    La primera línea contiene un número entero $T$ ($1 \leq T \leq 100$): el número de casos de prueba en la entrada. Luego siguen los casos de prueba $T$.
#    La primera línea contiene un número entero $T$ ($1 \leq T \leq 100$): el número de casos de prueba en la entrada. Luego siguen los casos de prueba $T$.
#    La primera línea contiene un número entero $T$ ($1 \leq T \leq 100$): el número de casos de prueba en la entrada. Luego siguen los casos de prueba $T$.
#    Cada caso de prueba consta de dos líneas.
#    Cada caso de prueba consta de dos líneas.
#    Cada caso de prueba consta de dos líneas.
#    La primera línea contiene un número entero positivo $n$ ($2 \leq n \leq 50$) - número de personas.
#    La primera línea contiene un número entero positivo $n$ ($2 \leq n \leq 50$) - número de personas.
#    La primera línea contiene un número entero positivo $n$ ($2 \leq n \leq 50$) - número de personas.
#    La segunda línea contiene $n$ enteros positivos $a_{0}$, $a_{1}$, ..., $a_{n-1}$($1 \leq a_{i}\leq 1000$), donde $a_{i}$es la fuerza de la $i$-ésima persona. Tenga en cuenta que los valores de $a_{i}$pueden no ser distintos.
#    La segunda línea contiene $n$ enteros positivos $a_{0}$, $a_{1}$, ..., $a_{n-1}$($1 \leq a_{i}\leq 1000$), donde $a_{i}$es la fuerza de la $i$-ésima persona. Tenga en cuenta que los valores de $a_{i}$pueden no ser distintos.
#    La segunda línea contiene $n$ enteros positivos $a_{0}$, $a_{1}$, ..., $a_{n-1}$($1 \leq a_{i}\leq 1000$), donde $a_{i}$es la fuerza de la $i$-ésima persona. Tenga en cuenta que los valores de $a_{i}$pueden no ser distintos.
#   Salida
#    Para cada caso de prueba, imprima un número entero: el valor mínimo de $|max(A) − min(B)|$ con la división óptima de todas las personas en dos equipos. Cada uno de las personas debe ser miembro de exactamente uno de los dos equipos.
#    Para cada caso de prueba, imprima un número entero: el valor mínimo de $|max(A) − min(B)|$ con la división óptima de todas las personas en dos equipos. Cada uno de las personas debe ser miembro de exactamente uno de los dos equipos.
#    Para cada caso de prueba, imprima un número entero: el valor mínimo de $|max(A) − min(B)|$ con la división óptima de todas las personas en dos equipos. Cada uno de las personas debe ser miembro de exactamente uno de los dos equipos.
#   Ejemplo Entrada
#    553 1 2 6 462 1 3 2 4 347 9 3 121 10003100 150 200
#   Ejemplo Salida
#    10299950
#   Ayuda
#    El primer caso de prueba se explicó en el enunciado. En el segundo caso de prueba, una de las divisiones óptimas es $A$ = [$2$,$1$], $B$ = [$3$,$2$,$4$,$3$], por lo que la respuesta es |$2$−$2$| = $0$.
#    El primer caso de prueba se explicó en el enunciado. En el segundo caso de prueba, una de las divisiones óptimas es $A$ = [$2$,$1$], $B$ = [$3$,$2$,$4$,$3$], por lo que la respuesta es |$2$−$2$| = $0$.
#    El primer caso de prueba se explicó en el enunciado. En el segundo caso de prueba, una de las divisiones óptimas es $A$ = [$2$,$1$], $B$ = [$3$,$2$,$4$,$3$], por lo que la respuesta es |$2$−$2$| = $0$.

n = int(input())
 
for i in range(n):
    tam = int(input())
    lista = list(map(int, input().split()))
    lista.sort()
    minimo = 100000000000000000000000
    for i in range(1,tam):
        a = lista[0:i]
        b = lista[i:tam]
        menor = max(a)-min(b)
        menor = abs(menor)
        if menor < minimo:
            minimo = menor
    print(f"{minimo}")