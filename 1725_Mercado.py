# https://jv.umsa.bo/oj/problem.php?id=1725
#  Mercado
#  Enviar
#  Estado
#  Descripción
#    El mercado Rodrigues el más grande de la ciudad y ofrece la más amplia variedad de comida.Hay mucha fruta y fuiste a comprar duraznos. El precio original es k bs. El segundo durazno cuesta 2k, y el tercero 2(2k), el cuarto 2(2(2k)) y así sucesivamente. Te encantan los duraznos y compraste varios. EL precio de cada durazno se calcula con la formula anterior. Te darán el monto total pagado T y el precio inicial. TU tarea es hallar el numero de duraznos que compraste.Por ejemplo si el valor inicial es 150 y pagaste 1050 el proceso es el siguiente150 + 2*150 + 2*2*150 = 150 + 300 + 600 = 1050.Que significa que compraste 3 duraznos.
#   Entrada
#    La entrada consiste en múltiples casos de prueba y termina cuando no hay más datos.Cada caso de prueba consiste de dos números enteros, K que esta entre 80 y 160. T esta entre 80 y 163,800.Se sabe que la respuesta existe y es un numero único.
#   Salida
#    En la salida por cada caso de prueba escriba un numero con el numero de duraznos que compro.
#   Ejemplo Entrada
#    100 100100 300150 1050160 163680
#   Ejemplo Salida
#    12310
#   Ayuda

# mercado
import sys

if __name__ == "__main__":
    for lin in sys.stdin:
        k, t = lin.split()
        k, t = int(k), int(t)
        z = k
        cont = 1
        while k != t:
            z *= 2
            k += (z)
            cont += 1
        print(cont)