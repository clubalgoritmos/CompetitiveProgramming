# https://jv.umsa.bo/oj/problem.php?id=1726
#  Productos
#  Enviar
#  Estado
#  Descripción
#    Dado un numero n se quieres multiplicar sus digitos, luego repetir sucesivamente hasta obtener un solo digito.Por ejemplo:n=77iteracion N multiplicación1 77 7*7=492 49 4*9=363 36 3*6=184 18 1*8=8Como se ve se hicierón 4 iteraciones para llegr a un numero de un solo digito.
#   Entrada
#    La entrada consiste en multiples casos de prueba. La primera línea indica el numero de casos de prueba.Lugo siguen los caos de prueba, cada caso consiste en un solo numero entero en una linea.
#   Salida
#    Por cada caso de prueba escriba la palabra pasos seguido del numero de iteraciones requeridas para llegar a un producto de un solo dígito como se mostró en el ejemplo.
#   Ejemplo Entrada
#    60102532744277777788888899
#   Ejemplo Salida
#    0 pasos1 pasos2 pasos2 pasos2 pasos11 pasos
#   Ayuda

# Productos

'''Funcion recursiva para multiplicar los digitos de un numero'''
def mul_digitos(n):
    if n//10 == 0:
        return n
    else:
        return mul_digitos(n//10)*(n%10)


casos = int(input())
for i in range(casos):
    n = int(input())
    cont = 0
    while n > 9:
        cont += 1
        n = mul_digitos(n)
    print(cont, "pasos")