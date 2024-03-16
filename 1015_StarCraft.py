# https://jv.umsa.bo/oj/problem.php?id=1015
#  StarCraft
#  Enviar
#  Estado
#  Descripción
#    Los Terrans están siendo atacados por los Protoss una raza de humanoides que aparecen en  la serie Star Craft.
#    Los Terrans ya casi sin tropas y con poca estructuras solo tienen una esperanza para vencer en esta guerra contra los Protoss. Y esa esperanza es poder usar el arma más poderosa que tienen,”la Bomba Nuclear“.
#    Para tal proposito necesitan un soldado que pueda marcar el blanco para el ataque nuclear y ese soldado es Ghost, un soldado capaz de volverse invisible y poder infiltrarse en la base de los Protoss
#    Ghost se dirige hacia la Base de los Protoss y logra infiltrarse en ella para así marcar el blanco del ataque Nuclear.
#    Ghost está tiene dudas al marcar el blanco para el ataque nuclear así que el pide tu ayuda para este problema.
#    Ghost te enviara coordenadas de cada estructura de la base Protoss. Así que él quiere saber el número de estructuras que serán destruidas dadas las coordenadas del blanco de la bomba nuclear y el radio de alcance de esta.
#   Entrada
#    La primera línea es un entero T (1<=T<=100) el número de casos de prueba. Seguidamente se te dará un entero N (1<=N<=100) el número de coordenadas x, y que te enviara Ghost.
#    A continuación vendrán N líneas, cada una de 2 valores x, y (0<=x, y<=1000) donde  cada una representa la coordenada de una estructura Protoss.
#    La última Linea tendrá 3 valores x, y, r. Donde x, y son las coordenadas del blanco del ataque nuclear y r (1<=r<=500) el radio de alcance de la bomba Nuclear.
#   Salida
#    Para cada caso de Prueba imprimir el número de estructuras Potross destruidas por la bomba Nuclear (Una estructura será destruida si la coordenada de la estructura Protoss está en el radio de alcance de la Bomba Nuclear)
#   Ejemplo Entrada
#    321 11 00 0 121 11 00 0 520 050 505 5 10
#   Ejemplo Salida
#    121
#   Ayuda
#    2da div. 2012 UMSA

for _ in range(int(input())):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    x0,y0,r = tuple(map(int, input().split()))
    c=0
    for i in range(N):
        x,y = arr[i]
        if (x-x0)**2 + (y-y0)**2 <= r**2:
            c+=1
    print(c)