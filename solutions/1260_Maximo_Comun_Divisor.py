# https://jv.umsa.bo/oj/problem.php?id=1260
#  Maximo Comun Divisor
#  Enviar
#  Estado
#  Descripción
#   Entrada
#    La primera línea contiene el numero $n$ de casos de prueba. Luego siguen $n$ lineas cada una con un caso de prueba. Cada caso de prueba contiene dos números enteros $a$ y $b$ separados por un espacio. $2 \leq a,b \leq 10^5$
#   Salida
#    Escriba en una linea el máximo común divisor entre $a$ y $b$.
#   Ejemplo Entrada
#    248 6042 56
#   Ejemplo Salida
#    1214
#   Ayuda

for _ in range(int(input())):
    a,b = map(int,input().split())
    def mcd(a,b):
        while b:
            a,b = b,a%b
        return a
    print(mcd(a,b))