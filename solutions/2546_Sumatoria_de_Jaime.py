# https://jv.umsa.bo/oj/problem.php?cid=2823&pid=15
## https://jv.umsa.bo/oj/problem.php?id=2546
#  Sumatoria de Jaime
#  Enviar
#  Estado
#  Descripción
#    Jaime es un niño obsesionado con un número, tanto que su nombre tiene esa cantidad de letras (cinco), ahora Jaime te reta a realizar un programa, donde está implicado su número favorito.
#    Dados 2 números (n, x) de entrada resolver la siguiente sumatoria para n términos:
#    $2\frac{x}{1} +3\frac{x^{2}}{2} + 5\frac{x^{3}}{3} + 7\frac{x^{4}}{6} + 11\frac{x^{5}}{12} + 13\frac{x}{24} + 17\frac{x^{2}}{47} + 19\frac{x^{3}}{92} + 23\frac{x^{4}}{181} + 29\frac{x^{5}}{356} + 31\frac{x}{700}+...$
#    Ayuda a Jaime
#   Entrada
#    La entrada consiste de varios casos de prueba, para cada caso de prueba se te darán 2 números en una misma línea separados por un espacio, estos números enteros serán n (1 ≤ n ≤ 120) y x (1 ≤ x ≤ 70) respectivamente.
#   Salida
#    Por cada caso de prueba muestre el resultado de la sumatoria con 2 decimales de precisión.
#   Ejemplo Entrada
#    2 32 12 7012 62 256 252 5
#   Ejemplo Salida
#    19.503.507490.009926.24987.509434594.7947.50
#   Ayuda

def next_prime(n):
    while True:
        n += 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                break
        else:
            return n

while True:
    try:
        lastprime = 1
        S = 0
        n,x = map(int,input().split())
        for i in range(n):

            S+=lastprime*(x**i)/lastprime
            lastprime = next_prime(lastprime)
        print("{:.2f}".format(S)) 
    except EOFError:
        break