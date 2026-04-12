# https://jv.umsa.bo/oj/problem.php?cid=2575&pid=7
## https://jv.umsa.bo/oj/problem.php?id=2128
#  Accidente de microondas
#  Estado
#  Descripción
#    Valentina tiene mucha hambre. Coge una cena que compro del supermercado, la mete en el microondas y registra en el microondas $02:15$ para cocinarla en $2$ minutos y $15$ segundos. Valentina desconoce que el microondas toma estos valores como horas y minutos, es decir, el microondas toma $02:15$ como $2$ horas y $15$ minutos (no $2$ minutos y $15$ segundos). Necesitamos indicarle a Valentina cuánto tiempo extra (es decir, tiempo adicional) tendrá que esperar hasta que se termine de cocinar su cena. Es decir, debemos decirle a Valentina que su comida estará lista en $2$ horas, $12$ minutos y $45$ segundos más de lo que ella esperaba.
#    Valentina tiene mucha hambre. Coge una cena que compro del supermercado, la mete en el microondas y registra en el microondas $02:15$ para cocinarla en $2$ minutos y $15$ segundos. Valentina desconoce que el microondas toma estos valores como horas y minutos, es decir, el microondas toma $02:15$ como $2$ horas y $15$ minutos (no $2$ minutos y $15$ segundos). Necesitamos indicarle a Valentina cuánto tiempo extra (es decir, tiempo adicional) tendrá que esperar hasta que se termine de cocinar su cena. Es decir, debemos decirle a Valentina que su comida estará lista en $2$ horas, $12$ minutos y $45$ segundos más de lo que ella esperaba.
#    Valentina tiene mucha hambre. Coge una cena que compro del supermercado, la mete en el microondas y registra en el microondas $02:15$ para cocinarla en $2$ minutos y $15$ segundos. Valentina desconoce que el microondas toma estos valores como horas y minutos, es decir, el microondas toma $02:15$ como $2$ horas y $15$ minutos (no $2$ minutos y $15$ segundos). Necesitamos indicarle a Valentina cuánto tiempo extra (es decir, tiempo adicional) tendrá que esperar hasta que se termine de cocinar su cena. Es decir, debemos decirle a Valentina que su comida estará lista en $2$ horas, $12$ minutos y $45$ segundos más de lo que ella esperaba.
#    El problema:Dado el tiempo inicial en la forma de $MM:SS$, donde la entrada se toma realmente como $HH:MM$, determine cuánto tiempo más estará su comida en el microondas. Proporcione esta información en forma de $HH:MM:SS$.
#    El problema:
#    El problema:
#    Dado el tiempo inicial en la forma de $MM:SS$, donde la entrada se toma realmente como $HH:MM$, determine cuánto tiempo más estará su comida en el microondas. Proporcione esta información en forma de $HH:MM:SS$.
#    Dado el tiempo inicial en la forma de $MM:SS$, donde la entrada se toma realmente como $HH:MM$, determine cuánto tiempo más estará su comida en el microondas. Proporcione esta información en forma de $HH:MM:SS$.
#   Entrada
#    La primera línea de la entrada contiene un número entero $t (1 \leq t \leq 100)$: el número de casos de prueba.
#    La primera línea de la entrada contiene un número entero $t (1 \leq t \leq 100)$: el número de casos de prueba.
#    La primera línea de la entrada contiene un número entero $t (1 \leq t \leq 100)$: el número de casos de prueba.
#    Cada caso de prueba constará de una sola línea en forma de $MM: SS$, que representa los valores que ingreso Valentina. $MM$ y $SS$ estarán en el rango de $00$ y $59$ (inclusive), pero ambos no serán $00$ al mismo tiempo, es decir, el tiempo total será positivo, es decir, que la entrada no será $00:00$.
#    Cada caso de prueba constará de una sola línea en forma de $MM: SS$, que representa los valores que ingreso Valentina. $MM$ y $SS$ estarán en el rango de $00$ y $59$ (inclusive), pero ambos no serán $00$ al mismo tiempo, es decir, el tiempo total será positivo, es decir, que la entrada no será $00:00$.
#    Cada caso de prueba constará de una sola línea en forma de $MM: SS$, que representa los valores que ingreso Valentina. $MM$ y $SS$ estarán en el rango de $00$ y $59$ (inclusive), pero ambos no serán $00$ al mismo tiempo, es decir, el tiempo total será positivo, es decir, que la entrada no será $00:00$.
#   Salida
#    Por cada caso de prueba:La salida debe contener una sola línea en forma de $HH:MM:SS$, que indica el tiempo adicional de cocimiento de los alimentos en el microondas. Tenga en cuenta que debe imprimir dos dígitos para cada parte. También tenga en cuenta que $MM$ y $SS$ deben estar en el rango de $00$ a $59$.
#    Por cada caso de prueba:
#    Por cada caso de prueba:
#    La salida debe contener una sola línea en forma de $HH:MM:SS$, que indica el tiempo adicional de cocimiento de los alimentos en el microondas. Tenga en cuenta que debe imprimir dos dígitos para cada parte. También tenga en cuenta que $MM$ y $SS$ deben estar en el rango de $00$ a $59$.
#    La salida debe contener una sola línea en forma de $HH:MM:SS$, que indica el tiempo adicional de cocimiento de los alimentos en el microondas. Tenga en cuenta que debe imprimir dos dígitos para cada parte. También tenga en cuenta que $MM$ y $SS$ deben estar en el rango de $00$ a $59$.
#   Ejemplo Entrada
#    305:0013:3700:10
#   Ejemplo Salida
#    04:55:0013:23:2300:09:50
#   Ayuda

for _ in range(int(input())):
    AA,BB = map(int,input().split(":"))
    SS = AA*60*60+BB*60
    SS -= AA*60+BB
    HH = SS // 3600
    MM = (SS % 3600) // 60
    SS = SS % 60

    print(f"{HH:02}:{MM:02}:{SS:02}")