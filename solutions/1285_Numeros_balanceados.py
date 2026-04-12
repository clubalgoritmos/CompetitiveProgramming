# https://jv.umsa.bo/oj/problem.php?id=1285
#  Numeros balanceados
#  Enviar
#  Estado
#  Descripción
#    En este ejercicio decimos que un numero es balanceado si la suma de sus dígitos en posiciones pares es igual a la suma de sus dígitos en posiciones impares.
#    (Si notamos en particular para este problema, da igual si contamos las posiciones de izquierda a derecha o de derecha a izquierda)
#   Entrada
#    La entrada consiste de múltiples casos de prueba. Cada caso de prueba es un numero entero positivo. Termina cuando no hay más datos.
#   Salida
#    Escriba en una linea si es un numero balanceado.
#   Ejemplo Entrada
#    14634801512345
#   Ejemplo Salida
#    SISINO
#   Ayuda

while True:
    try:
        if sum([a*(-1)**i for i,a in enumerate(map(int,input()))]) == 0:
            print("SI")
            continue
        print("NO")
    except EOFError:
        break