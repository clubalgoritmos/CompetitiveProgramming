# https://jv.umsa.bo/oj/problem.php?id=1808
#  Amor en tiempos de minecraft
#  Enviar
#  Estado
#  Descripción
#    En un pequeño mundo de minecraft existen muchos aldeanos pero nos enfocaremos en alguien en especial llamado Mike y, quien se había enamorado profundamente de una aldeana llamada Michelle y quería vivir cerca de ella a toda costa.
#    En un pequeño mundo de minecraft existen muchos aldeanos pero nos enfocaremos en alguien en especial llamado Mike y, quien se había enamorado profundamente de una aldeana llamada Michelle y quería vivir cerca de ella a toda costa.
#    En la aldea donde vive Michelle, existen terrenos que pueden ser de diferente tamaño, cada terreno está separado por 10 metros, en algunos terrenos existen casitas que ya están construidas y por supuesto Mike no puede construir una casita en esos terrenos ocupados.
#    En la aldea donde vive Michelle, existen terrenos que pueden ser de diferente tamaño, cada terreno está separado por 10 metros, en algunos terrenos existen casitas que ya están construidas y por supuesto Mike no puede construir una casita en esos terrenos ocupados.
#    Los terrenos están alineados de izquierda a derecha por lo que la casa del extremo a la izquierda será la casa 1, a lado la casa 2, y así hasta la casa n.
#    Los terrenos están alineados de izquierda a derecha por lo que la casa del extremo a la izquierda será la casa 1, a lado la casa 2, y así hasta la casa n.
#    Michelle vive en la posición m. Se te darán n enteros a1, a2, a3,... an que denotan si un terreno está disponible para su construcción y la cantidad de recursos que se necesitan para que se pueda construir en ello una casita, si ai es igual a 0 significa que una casita ya está construida en ese lugar y por lo tanto, no se puede construir una casita en ese espacio .
#    Entonces, Mike tiene k recursos y debe elegir con cuidado en que terreno debe construir una casita que esté cerca de Michelle. Ayuda a Mike a determinar la distancia mínima entre la casa de Michelle y el terreno donde puede construir su casita y ayudarlo a que su amor suceda.
#    Entonces, Mike tiene k recursos y debe elegir con cuidado en que terreno debe construir una casita que esté cerca de Michelle. Ayuda a Mike a determinar la distancia mínima entre la casa de Michelle y el terreno donde puede construir su casita y ayudarlo a que su amor suceda.
#    Entonces, Mike tiene k recursos y debe elegir con cuidado en que terreno debe construir una casita que esté cerca de Michelle. Ayuda a Mike a determinar la distancia mínima entre la casa de Michelle y el terreno donde puede construir su casita y ayudarlo a que su amor suceda.
#    Entonces, Mike tiene k recursos y debe elegir con cuidado en que terreno debe construir una casita que esté cerca de Michelle. Ayuda a Mike a determinar la distancia mínima entre la casa de Michelle y el terreno donde puede construir su casita y ayudarlo a que su amor suceda.
#   Entrada
#    La primera línea contiene tres enteros n, m y k (2≤n≤100, 1≤m≤n, 1≤k≤100) que representan: el número de terrenos en la aldea, la casa donde vive Michelle y la cantidad de recursos que dispone Mike.
#    La primera línea contiene tres enteros n, m y k
#    (
#    2≤
#    n
#    ≤100
#    ,
#    1≤
#    m
#    ≤
#    n
#    ,
#    1≤
#    k
#    ≤100
#    ) que representan: el número de terrenos en la aldea, la casa donde vive Michelle y la cantidad de recursos que dispone Mike.
#    La segunda línea contiene n enteros a1, a2,..., an (0≤ai≤100) denotando la disponibilidad y la cantidad de recursos que se necesitan para construir una casita.
#    La segunda línea contiene n enteros a1, a2,..., an (
#    0≤
#    a
#    i
#    ≤100
#    ) denotando la disponibilidad y la cantidad de recursos que se necesitan para construir una casita.
#    Es garantía que am = 0 y tener en cuenta que no se puede construir una casita con más de k recursos.
#    Es garantía que am = 0 y tener en cuenta que no se puede construir una casita con más de k recursos.
#   Salida
#    Imprimir un entero que indique la mínima distancia en metros desde la casa de Michelle hasta la casa que Mike puede comprar.
#    Imprimir un entero que indique la mínima distancia en metros desde la casa de Michelle hasta la casa que Mike puede comprar.
#    Imprimir un entero que indique la mínima distancia en metros desde la casa de Michelle hasta la casa que Mike puede comprar.
#   Ejemplo Entrada
#    5 1 200 27 32 21 19
#   Ejemplo Salida
#    40
#   Ayuda

n, m, k = map(int, input().split())
m-=1
a = list(map(int, input().split()))
left = next((i for i in range(m-1, -1, -1) if a[i] <= k and a[i]!=0), float('inf'))
right = next((i for i in range(m+1, len(a), 1) if a[i] <= k and a[i]!=0), float('inf'))
print((min(abs(left-m),abs(right-m)))*10)