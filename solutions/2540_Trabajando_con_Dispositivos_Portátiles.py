# https://jv.umsa.bo/oj/problem.php?id=2540
#  Trabajando con Dispositivos Portátiles
#  Enviar
#  Estado
#  Descripción
#    En la zona de Villa Esperanza, donde está ubicada la UPEA, hay una red de dispositivos portátiles que opera de la siguiente manera:
#    El área está dividida en casillas que forman una matriz de SxS con filas y columnas numeradas de 0 a S-1.
#    Cada casilla obtiene una estación local. El número de dispositivos portátiles puede cambiar dentro de una misma casilla, porque los dispositivos pueden ser movidos de una casilla a otra, o pueden ser prendidos o finalmente apagados.
#    Una estación local puede reportar cambios en el número de dispositivos activos, enviando su fila y su columna a la estación principal.
#    Escribe un programa que reciba los reportes y, responda preguntas acerca del total de dispositivos portátiles activos en cualquier región rectangular.
#   Entrada
#    Línea 1:
#    Contendrá un único entero indicando el valor de
#    S
#    Siguientes líneas:
#    Cada línea puede representar o una pregunta o un reporte.
#    Si la línea representa un reporte, contendrá el caracter 1 seguido de 3 enteros X Y A indicando que a la posición (X,Y) se sumaron A aparatos portátiles (nótese que A puede ser negativo).
#    Si la línea representa una pregunta, contendrá el caracter 2 seguido de 4 enteros L B R y T, indicando la pregunta "Cuántos aparatos activos hay en las casillas (X,Y) donde L<= X<=R y B<=Y<=T
#    Última línea:
#    Contendrá solamente el caracter
#    3
#   Salida
#    Imprime el resultado a cada línea de consulta que tenía el caracter 2.
#    Imprime el resultado a cada línea de consulta que tenía el caracter 2.
#   Ejemplo Entrada
#    41 1 2 32 0 0 2 21 1 1 21 1 2 -12 1 1 2 33
#   Ejemplo Salida
#    34
#   Ayuda
#    El tamaño del área será entre: 1 <= S <= 1024
#    La entrada no contendrá más de 65 mil líneas.
#    Los valores absolutos de los número de cada casilla nunca superarán 40 mil.
#    En la tabla completa habrá a los más 230 dispositivos.

s = int(input())
M = list()
for i in range(s):
    M.append([0]*s)

while True:
  V = [int(x) for x in input().split(' ')]
  if V[0] == 1:
    M[V[1]][V[2]] = M[V[1]][V[2]]+V[3]
  elif V[0] == 2:
    s = 0
    for i in range(V[2], V[4]+1, 1):
      for j in range(V[1], V[3]+1, 1):
        s = s + M[i][j]
    print(s)
  elif V[0] == 3:
    break