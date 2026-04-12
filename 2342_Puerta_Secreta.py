# https://jv.umsa.bo/oj/problem.php?cid=2820&pid=2
## https://jv.umsa.bo/oj/problem.php?id=2342
#  Puerta Secreta
#  Enviar
#  Estado
#  Descripción
#    Autor: Miguel Ortiz
#    Cody es un arqueologo con fama mundial, es principalmente conocido por el descubrimiento de la puerta a la Atlantida en medio del lago Titicaca. Lleva años descifrando el misterio para abrir la puerta y hoy por fin lo logro, un número $n$ es la clave para hacerlo.Reune a todo su equipo, se dirigen a la antigua puerta y todos miran asombrados mientras Cody la abre lentamente. Por desgracia para todos, lo que hay detras no es la Atlantida, ¡es otra puerta! Esta puerta tiene una sola inscripcion, el acertijo para abrirla es:
#    2 **a ∗ 3 **b ∗ 5** c ∗ 7 **d ≡ 0 (mod n)Cody lo reconoce, ya lo ha visto antes y sabe que debe conseguir lo siguiente: $a$ artefactos del primer tipo, b del segundo, c del tercero y d del cuarto, de forma que los valores de a, b, c y d resuelvan la congruencia escrita en la puerta.Para conseguir cada artefacto hay que viajar por el mundo, y aun asi, no hay seguridad de que exista alguna configuracion de valores que abran la puerta. Por esto pide la ayuda de los programadores del equipo, para viajar lo menos posible o determinar que es imposible abrirla.Dado un numero n se debe calcular la menor suma a + b + c + d de valores que cumplan la con la congruencia o indicar que no existe una solucion.
#   Entrada
#    La primera y unica linea contendra un numero entero n (1 <= n <= 10** 5 ).
#   Salida
#    Un solo numero entero, indicando la menor suma a + b + c + d tal que cumplanla congruencia. Imprimir −1 si no existe una solucion.
#   Ejemplo Entrada
#    30
#   Ejemplo Salida
#    3
#   Ayuda

N = int(input())

factors = [2, 3, 5, 7]
counts = [0, 0, 0, 0]
for i, factor in enumerate(factors):
    while N % factor == 0:
        counts[i] += 1
        N /= factor
if N != 1:
    print(-1)
    exit()
print(sum(counts))
