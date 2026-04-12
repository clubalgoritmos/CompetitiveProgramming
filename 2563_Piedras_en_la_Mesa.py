# https://jv.umsa.bo/oj/problem.php?id=2563
#  Piedras en la Mesa
#  Enviar
#  Estado
#  Descripción
#    Dereck encuentra en la mesa del comedor, N piedras de colores Rojo, Verde y Azul, ordenadas en una fila. Se le ocurrió un interesante problema para programar, contando cuántas piedras del mismo color están juntas.
#    Dereck encuentra en la mesa del comedor, N piedras de colores Rojo, Verde y Azul, ordenadas en una fila. Se le ocurrió un interesante problema para programar, contando cuántas piedras del mismo color están juntas.
#    Dereck encuentra en la mesa del comedor, N piedras de colores Rojo, Verde y Azul, ordenadas en una fila. Se le ocurrió un interesante problema para programar, contando cuántas piedras del mismo color están juntas.
#   Entrada
#    La primera línea contiene un valorN(1≤N≤50) que corresponde al número de piedras. La siguiente línea contiene una cadenaSque representa a los colores de las piedras,Rpara las rojas,Vpara las verdes yApara las azules.
#    La primera línea contiene un valorN(1≤N≤50) que corresponde al número de piedras. La siguiente línea contiene una cadenaSque representa a los colores de las piedras,Rpara las rojas,Vpara las verdes yApara las azules.
#    La primera línea contiene un valor
#    (1≤N≤50) que corresponde al número de piedras. La siguiente línea contiene una cadena
#    que representa a los colores de las piedras,
#    para las rojas,
#    para las verdes y
#    para las azules.
#   Salida
#    Imprime sólo un entero, que corresponde a la cantidad de piedras contadas del mismo color que se encuentran juntas.
#    Imprime sólo un entero, que corresponde a la cantidad de piedras contadas del mismo color que se encuentran juntas.
#    Imprime sólo un entero, que corresponde a la cantidad de piedras contadas del mismo color que se encuentran juntas.
#   Ejemplo Entrada
#    8VVAARRRR
#   Ejemplo Salida
#    5
#   Ayuda

n = int(input())
P = [x for x in input().upper()]
s = 0
for i in range(1, n):
  if P[i-1] == P[i]:
    s+=1
print(s)