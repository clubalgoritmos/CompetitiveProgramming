# https://jv.umsa.bo/oj/problem.php?id=1268
## https://jv.umsa.bo/oj/problem.php?id=1268
#  Granja
#  Enviar
#  Estado
#  Descripción
#    Juan y José tienen una granja de gallinas y vacas, un día se les ocurrió contar el número de cabezas y el número de patas de los animales (vacas y gallinas) en la granja. Juan contó un total de 3 cabezas y José contó un total de 8 patas del total de animales en la granja. Juan hizo algunos cálculos y determino que existen 2 gallinas y 1 vaca. José noto que Juan tarda demasiado en hacer los cálculos, así que pide tu ayuda para poder obtener una solución general del problema.Nota: Una gallina tiene 1 cabeza y 2 patas. Una vaca tiene 1 cabeza y 4 patas. Si la solución existe, esta siempre es única.
#   Entrada
#    La entrada contiene varias líneas, cada una con dos numeros, el número de cabezas $X$ ($1 <= X <= 50$) y el número de patas $Y$($1 <= Y <= 50$). La entrada termina con $X=0$,$Y=0$ (El cual no debe ser procesado)
#   Salida
#    Por cada caso de entrada, escriba en la salida, separados por un espacio, el número de gallinas y el número de vacas respectivamente. En caso de no existir solución imprimir -1.
#   Ejemplo Entrada
#    3 810 401 30 0
#   Ejemplo Salida
#    2 10 10-1
#   Ayuda

while True:
    X,Y = map(int,input().split())
    if X==0 and Y==0:
        break
    if (Y-2*X)%2==0 and (4*X-Y)%2==0 and (Y-2*X)>=0 and (4*X-Y)>=0:
        print((4*X-Y)//2,(Y-2*X)//2)
    else:
        print(-1)