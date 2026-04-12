# https://jv.umsa.bo/oj/problem.php?cid=2819&pid=6
## https://jv.umsa.bo/oj/problem.php?id=1401
#  Concurso de Televisión
#  Enviar
#  Estado
#  Descripción
#    Con la finalidad de atraer a mayor audiencia el canal de TV de su localidad ha decidido crear un concurso en el que va regalar dinero a los participantes.El concurso consiste de una caja rectangular de bolas, donde cada bola tiene un numero enteroque está en el rango ($-100 \leq n \ 100$). El concursante debe escoger un rango de bolas de la base y obtiene un premio en dinero equivalente a la suma de todas las bolas del rango que escogió y de todas las que están por encima de estas bolas.Por ejemplo, si tenemos una caja con las bolas como se muestra en la figura:
#    Si escoge de las 6 columnas las que corresponden al rango rango de 1 a 5 se lleva el dinero que corresponde a las columnas 1,2,3,4,5 haciendo un total de 16 pesos.Para no perder dinero en el concurso te piden hallar el máximo de dinero que un concursante puede obtener.
#   Entrada
#    La entrada consiste de varios casos de prueba. La primera linea de cada caso de prueba tiene dos números que son las dimensiones de la matriz n,m, ($1 \leq n,m \leq 100000$).Luego siguen $n$ filas cada una con $m$ números separados por espacio.
#   Salida
#    Escriba en la salida el máximo numero de pesos que un concursante puede ganar.
#   Ejemplo Entrada
#    3 65 -1 -10 4 -1 31 -1 17 -2 3 17 -1 -8 4 -1 -8
#   Ejemplo Salida
#    16
#   Ayuda

n, m = map(int, input().split())
A = [0]*m
for _ in range(n):
    row = list(map(int, input().split()))
    for i in range(m):
        A[i] += row[i]

max_so_far = A[0]
max_ending_here = 0

for i in range(0, m):
    max_ending_here = max_ending_here + A[i]
    if max_so_far < max_ending_here:
        max_so_far = max_ending_here
    if max_ending_here < 0:
        max_ending_here = 0
print(max_so_far)