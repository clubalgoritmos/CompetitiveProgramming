# https://jv.umsa.bo/oj/problem.php?id=1014
#  Marisol la exploradora
#  Enviar
#  Estado
#  Descripción
#    A Marisol le gusta visitar los lugares turísticos, hoy le toca conocer la ciudad de La Paz, una de las más conflictivas en Bolivia ya que hay marchas, bloqueos y no todas las calles son de doble sentido, existen N lugares turísticos y M rutas que conectan dichos sitios, ella quiere conocer los N lugares sin importar el orden.
#    A Marisol le gusta visitar los lugares turísticos, hoy le toca conocer la ciudad de La Paz, una de las más conflictivas en Bolivia ya que hay marchas, bloqueos y no todas las calles son de doble sentido, existen N lugares turísticos y M rutas que conectan dichos sitios, ella quiere conocer los N lugares sin importar el orden.
#    Marisol necesita tu ayuda para saber si puede llegar de cualquier sitio a cualquier otro.
#    Marisol necesita tu ayuda para saber si puede llegar de cualquier sitio a cualquier otro.
#   Entrada
#    La entrada consiste en varios casos de prueba, cada caso de prueba esta dado como sigue:
#    La entrada consiste en varios casos de prueba, cada caso de prueba esta dado como sigue:
#    Dos enteros N, M (1<=N<=2000)seguido de M líneas, en cada línea dos enteros X, Y  que quiere decir que se puede ir de X a Y (eso no implica que dé Y a X exista una ruta)
#    Dos enteros N, M (1<=N<=2000)seguido de M líneas, en cada línea dos enteros X, Y  que quiere decir que se puede ir de X a Y (eso no implica que dé Y a X exista una ruta)
#    La entrada de datos termina con N=0 y M=0
#    La entrada de datos termina con N=0 y M=0
#   Salida
#    Si se puede llegar de todos los lugares a todos los lugares imprime SI, caso contrario imprima NO
#    Si se puede llegar de todos los lugares a todos los lugares imprime SI, caso contrario imprima NO
#   Ejemplo Entrada
#    3  11  23  31  22  33  12  11  20  0
#   Ejemplo Salida
#    NOSINO
#   Ayuda
#    2da div. 2013 UMSA

while True:
    N,M = map(int,input().split())
    if N==0 and M==0:
        break
    graph = {i:set() for i in range(1,N+1)}
    for _ in range(M):
        a,b = map(int,input().split())
        graph[a].add(b)
    for i in range(1,N+1):
        visited = [False for _ in range(N+1)]
        stack = [i]
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            for child in graph[node]:
                stack.append(child)
        if not all(visited[1:]):
            print("NO")
            break
    else:
        print("SI")