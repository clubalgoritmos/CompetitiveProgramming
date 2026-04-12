# https://jv.umsa.bo/oj/problem.php?id=1736
## https://jv.umsa.bo/oj/problem.php?id=1736
#  Numeros de Fermat
#  Enviar
#  Estado
#  Descripción
#    Genere N números de Fermat, estos son números de la forma Fn = 22^n + 1, desde n = 0 en adelante. Los primeros son:tos son números de la forma Fn = 22^n + 1, desde n = 0 en adelante. Los primeros son:
#    F0 = 22^0 + 1 = 3F1 = 22^1 + 1 = 5F2 = 22^2 + 1 = 17F3 = 22^3 + 1 = 257F4 = 22^4 + 1 = 65537
#   Entrada
#    Un número N entero mayor a 0
#   Salida
#    Imprima en una sola linea los primero N números de Fermat en una sola línea. No debe imprimir un espacio despues del ultimo numero.
#   Ejemplo Entrada
#    3
#   Ejemplo Salida
#    3 5 17
#   Ayuda

N = int(input())
fermat = lambda n: 2**(2**n)+1
for i in range(N):
    print(fermat(i), end=" " if i < N-1 else "\n")