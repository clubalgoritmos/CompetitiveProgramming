# https://jv.umsa.bo/oj/problem.php?id=2539
#  Las visitas de Adriana
#  Enviar
#  Estado
#  Descripción
#    Adriana decidió visitar a su amiga. Considera el hecho de que la casa de Adriana está ubicada en el punto 0 y la casa de su amiga, está ubicada en el punto x (x>0) de la línea de coordenadas. En un solo salto, Adriana puede moverse 1, 2, 3, 4 o 5 posiciones hacia adelante. Determina cuál es el número mínimo de saltos que debe dar Adriana para llegar a la casa de su amiga.
#   Entrada
#    La primera línea de la entrada contiene un número entero X (1≤x≤1000000) — Que corresponde a la coordenada de la casa de la amiga.
#   Salida
#    Imprime el número mínimo de saltos que debe dar Adriana para ir del punto 0 al punto X.
#   Ejemplo Entrada
#    12
#   Ejemplo Salida
#    3
#   Ayuda

n = int(input())
s = n//5
n = n%5
s = s + n//4
n = n%4
s = s + n//3
n = n%3
s = s + n//2
n = n%2
s = s + n
print(s)