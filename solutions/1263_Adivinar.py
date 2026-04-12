# https://jv.umsa.bo/oj/problem.php?id=1263
#  Adivinar
#  Enviar
#  Estado
#  Descripción
#    Un juego de adivinanzas muy popular es suponga el número, donde una persona selecciona un número en un rango conocido, y otra persona intenta descubrir que número es. Después de cada intento, la primera persona revela si la suposición era correcta, demasiado alta, o demasiado baja.Muy pronto uno aprende que la mejor estrategia es suponer el número medio entre los cuales aún no han sido descartados. Si no existe un único número medio, entonces existen dos números para seleccionar. En ese caso, nosotros seleccionamos el más pequeño de esos números.El algoritmo se puede describir así:extremo inferior y limite superiorRepetir x = ( el extremo inferior + el límite superior )/2  (redondee hacia abajo si es necesario) Haga x su suposición Si x es demasiado baja, establezca extremo inferior a x+1 Si x es demasiado alta, establezca límite superior a x-1Hasta que x sea correctoPor ejemplo, suponga que los límites inferior y superior son $1$ y $9$ , respectivamente. El valor medio es $5$. Si esto es \textit{demasiado bajo}, los nuevos límites se convierten en $6$ y $9$. Este rango contiene cuatro números, y como no existe ningún número medio único. De los dos números en el centro que son $7$ y $8$ escogemos el más pequeño de éstos que es $7$ , así nuestra suposición próxima entonces se convierte en $7$.Construya un programa que permita leer el límite superior del rango (el extremo inferior siempre es $1$), y el número seleccionado por la primera persona. El programa deberá devolver un entero que representa el número total de intentos requerido por la segunda persona para adivinar el número correcto.
#   Entrada
#    La entrada consiste de varios casos de prueba. Cada caso de prueba consiste de dos números el número superior $1 \leq s \leq 1000$ y el número escogido $1 \leq e \leq s$. La entrada termina cuando no hay más datos.
#   Salida
#    Por cada caso de prueba escriba en la salida un solo número que indica el mínimo numero intentos para adivinar el número escogido.
#   Ejemplo Entrada
#    9 61000 750643 327157 157128 64
#   Ejemplo Salida
#    32781
#   Ayuda

while True:
    try:
        a,b = map(int,input().split())
        while True:
            x = a+b//2
    except EOFError:
        break