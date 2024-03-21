# https://jv.umsa.bo/oj/problem.php?cid=2575&pid=11
#  MichiTruco
#  Estado
#  Descripción
#    Hay una isla habitada por solo Michis, estos michis han logrado una sociedad tan avanzada que tienen muchos idiomas(MichiIdiomas) con los cual comunicarse.
#    Hay una isla habitada por solo Michis, estos michis han logrado una sociedad tan avanzada que tienen muchos idiomas(MichiIdiomas) con los cual comunicarse.
#    La isla de los Michis tiene $n$ Michis. Estos Michis pueden utilizar $m$ idiomas oficiales aprobados por el consejo oficial de Michis. Los idiomas se enumeran con números enteros del $1$ al $m$. Para cada Michi tenemos la lista de idiomas que conoce. Esta lista podría estar vacía, un Michi puede no saber idiomas que no hayan sido aprobados por el consejo oficial de Michis. Pero los Michis están dispuestos a aprender cualquier número de idiomas oficiales, siempre y cuando alguien se los pague sus lecciones. Un curso de estudio en un idioma para un Michi cuesta 1 michidolar.
#    La isla de los Michis tiene $n$ Michis. Estos Michis pueden utilizar $m$ idiomas oficiales aprobados por el consejo oficial de Michis. Los idiomas se enumeran con números enteros del $1$ al $m$. Para cada Michi tenemos la lista de idiomas que conoce. Esta lista podría estar vacía, un Michi puede no saber idiomas que no hayan sido aprobados por el consejo oficial de Michis. Pero los Michis están dispuestos a aprender cualquier número de idiomas oficiales, siempre y cuando alguien se los pague sus lecciones. Un curso de estudio en un idioma para un Michi cuesta 1 michidolar.
#    La isla de los Michis tiene $n$ Michis. Estos Michis pueden utilizar $m$ idiomas oficiales aprobados por el consejo oficial de Michis. Los idiomas se enumeran con números enteros del $1$ al $m$. Para cada Michi tenemos la lista de idiomas que conoce. Esta lista podría estar vacía, un Michi puede no saber idiomas que no hayan sido aprobados por el consejo oficial de Michis. Pero los Michis están dispuestos a aprender cualquier número de idiomas oficiales, siempre y cuando alguien se los pague sus lecciones. Un curso de estudio en un idioma para un Michi cuesta 1 michidolar.
#    Como tu eres un gran fan de los Michis y quieres verlos feli, encuentra la cantidad mínima de dinero que necesitas gastar para que cualquier Michi pueda corresponder a cualquier otro Michi(su correspondencia puede ser indirecta, es decir, otros Michis pueden ayudar traduciendo).
#    Como tu eres un gran fan de los Michis y quieres verlos feli, encuentra la cantidad mínima de dinero que necesitas gastar para que cualquier Michi pueda corresponder a cualquier otro Michi(su correspondencia puede ser indirecta, es decir, otros Michis pueden ayudar traduciendo).
#   Entrada
#    La primera línea contiene dos números enteros $n$ y $m$ $(2≤n,m≤100)$, el número de Michis y el número de idiomas.
#    La primera línea contiene dos números enteros $n$ y $m$ $(2≤n,m≤100)$, el número de Michis y el número de idiomas.
#    La primera línea contiene dos números enteros $n$ y $m$ $(2≤n,m≤100)$, el número de Michis y el número de idiomas.
#    Luego siguen $n$ líneas: la lista de idiomas de cada Michi.
#    Luego siguen $n$ líneas: la lista de idiomas de cada Michi.
#    Luego siguen $n$ líneas: la lista de idiomas de cada Michi.
#    Al comienzo de la $i$-ésima línea se encuentra un número entero $k_{i}$ $(0≤k_{i}≤m)$: la cantidad de idiomas que conoce el $i$-ésimo Michi.
#    Al comienzo de la $i$-ésima línea se encuentra un número entero $k_{i}$ $(0≤k_{i}≤m)$: la cantidad de idiomas que conoce el $i$-ésimo Michi.
#    Al comienzo de la $i$-ésima línea se encuentra un número entero $k_{i}$ $(0≤k_{i}≤m)$: la cantidad de idiomas que conoce el $i$-ésimo Michi.
#    A continuación, la $i$-ésima línea contiene $k_{i}$ enteros: $a_{ij}$ $(1\leqa_{ij}\leqm)$ , los identificadores de los idiomas que conoce el $i$-ésimo Michi.
#    A continuación, la $i$-ésima línea contiene $k_{i}$ enteros: $a_{ij}$ $(1\leqa_{ij}\leqm)$ , los identificadores de los idiomas que conoce el $i$-ésimo Michi.
#    A continuación, la $i$-ésima línea contiene $k_{i}$ enteros: $a_{ij}$ $(1\leqa_{ij}\leqm)$ , los identificadores de los idiomas que conoce el $i$-ésimo Michi.
#    Se garantiza que todos los identificadores en una lista son distintos. Tenga en cuenta que un Michi puede no saber ningún idioma.
#    Se garantiza que todos los identificadores en una lista son distintos. Tenga en cuenta que un Michi puede no saber ningún idioma.
#    Se garantiza que todos los identificadores en una lista son distintos. Tenga en cuenta que un Michi puede no saber ningún idioma.
#    Los números en las líneas están separados por espacios simples.
#    Los números en las líneas están separados por espacios simples.
#   Salida
#    Imprima un solo número entero: la cantidad mínima de dinero(michidolares) a pagar para que al final cada Michi pueda escribir una carta a cada uno (otros Michis pueden ayudar a traducir).
#    Imprima un solo número entero: la cantidad mínima de dinero(michidolares) a pagar para que al final cada Michi pueda escribir una carta a cada uno (otros Michis pueden ayudar a traducir).
#   Ejemplo Entrada
#    5 51 22 2 32 3 42 4 51 5
#   Ejemplo Salida
#    0 michidolares
#   Ayuda
#    Ejemplo entrada 2:
#    Ejemplo entrada 2:
#    Ejemplo entrada 2:
#    8 7
#    8 7
#    0
#    0
#    3 1 2 3
#    3 1 2 3
#    1 1
#    1 1
#    2 5 4
#    2 5 4
#    2 6 7
#    2 6 7
#    1 3
#    1 3
#    2 7 4
#    2 7 4
#    1 1
#    1 1
#    Ejemplo salida 2:
#    Ejemplo salida 2:
#    Ejemplo salida 2:
#    2 michidolares
#    2 michidolares
#    Ejemplo entrada 3:
#    Ejemplo entrada 3:
#    Ejemplo entrada 3:
#    2 2
#    2 2
#    1 2
#    1 2
#    0
#    0
#    Ejemplo salida 3:
#    Ejemplo salida 3:
#    Ejemplo salida 3:
#    1 michidolares
#    1 michidolares
#    En el segundo ca
#    En el segundo ca
#    so de entrada, el Michi $1$ puede aprender el idioma $2$ y el Michi $8$ puede aprender el idioma $4$.
#    so de entrada, el Michi $1$ puede aprender el idioma $2$ y el Michi $8$ puede aprender el idioma $4$.
#    En el tercer caso de entrada el Michi $2$ debe aprender el idioma $2$.
#    En el tercer caso de entrada el Michi $2$ debe aprender el idioma $2$.

n,m = map(int,input().split())
graph = dict()
for ni in range(n):
    arg = set(list(map(int,input().split()))[1:])
    graph[ni] = arg

print(graph)