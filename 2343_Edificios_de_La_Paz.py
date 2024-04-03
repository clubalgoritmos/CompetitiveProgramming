# https://jv.umsa.bo/oj/problem.php?cid=2819&pid=4
## https://jv.umsa.bo/oj/problem.php?id=2343
#  Edificios de La Paz
#  Enviar
#  Estado
#  Descripción
#    Hay $n$ edificios de bloques en una fila en la ciudad de La Paz, donde el edificio $i$ tiene una altura de $a_{i}$ bloques. Formas parte de un equipo de construcción y quieres que los edificios paceños se vean lo más bonitos posible. En un solo día, puede realizar la siguiente operación:
#    Elija dos índices $i$ y $j$ ($1 ≤ i, j \leq n$; $i ≠ j$) y mueva un bloque del edificio $i$ al edificio $j$. Esto esencialmente disminuye $a_{i}$ en $1$ y aumenta $a_{j}$ en $1$.
#    Crees que la fealdad de los edificios es la diferencia de altura entre los edificios más altos y los más bajo. Formalmente, la fealdad se define como $max(a) − min(a)$.
#    ¿Cuál es la fealdad mínima posible que puedes lograr después de varios días?
#   Entrada
#    La primera línea contiene un número entero $t$ ($1 \leq t \leq 1000$): el número de casos de prueba. Luego siguen $t$ casos.
#    La primera línea de cada caso de prueba contiene un número entero $n$ ($2 \leq n \leq 100$): el número de edificios en una fila de la ciudad de La Paz.
#    La segunda línea de cada caso de prueba contiene $n$ números enteros separados por espacios $a_{1}$, $a_{2}$,…, $a_{n}$ ($1 \leq a_{i} \leq 10^{7}$) - las alturas de los edificios.
#   Salida
#    Para cada caso de prueba, genere un único entero: la fealdad mínima posible de los edificios.
#   Ejemplo Entrada
#    3310 10 1043 2 1 251 2 3 1 5
#   Ejemplo Salida
#    001
#   Ayuda
#    En el primer caso de prueba, la fealdad ya es $0$.
#    En el segundo caso de prueba, debe realizar una operación, con $i = 1$ y $j = 3$. Las nuevas alturas ahora serán $[2,2,2,2]$, con una fealdad de $0$.
#    En el tercer caso de prueba, puede realizar tres operaciones:
#    con $i = 3$ y $j = 1$. El nuevo vector ahora será $[2,2,2,1,5]$,
#    La fealdad resultante es $1$. Se puede demostrar que esta es la fealdad mínima posible para esta prueba.

for _  in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = 0
    while True:
        if max(a)-min(a)<=1:
            break
        c += 1
        i = a.index(max(a))
        j = a.index(min(a))
        a[i] -= 1
        a[j] += 1
    print(c)