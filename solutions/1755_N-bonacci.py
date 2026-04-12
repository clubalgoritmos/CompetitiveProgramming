# https://jv.umsa.bo/oj/problem.php?id=1755
#  N-bonacci
#  Enviar
#  Estado
#  Descripción
#   Entrada
#   Salida
#    Por cada caso de prueba escriba en la salida un número con solicitado.
#   Ejemplo Entrada
#    34 27 37 5
#   Ejemplo Salida
#    53117
#   Ayuda



for _ in range(int(input())):
    i,n = map(int, input().split()) #elem, tipo
    fibo = [1]*n
    def fibonacci(i):
        if i < len(fibo):
            return fibo[i]
        fibo.append(sum(fibo[-n:]))
        return fibonacci(i)
    print(fibonacci(i))
