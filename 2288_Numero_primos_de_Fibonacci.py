# https://jv.umsa.bo/oj/problem.php?cid=2890&pid=0
## https://jv.umsa.bo/oj/problem.php?id=2288
#  Numero primos de Fibonacci
#  Enviar
#  Estado
#  Descripción
#    Un numero primo de Fibonacci es un número de la secuencia de Fibonacci que es primo.
#    Un numero primo de
#    Fibonacci
#    es un número de la secuencia de
#    que es primo.
#    Tomando los primeros dos números de Fibonacci $f_0=0,f_1=f_2=1$ la secuencia queda como sigue:
#    Tomando los primeros dos números de
#    $f_0=0,f_1=f_2=1$
#    la secuencia queda como sigue:
#    0   1   2  3  4  5  6  7  8   9  10  11
#    0   1   1  2  3  5  8  13 21 34  55  89
#    Como se ve los números correspondientes a las posiciones 3,5,7,11 son números primos.
#    La entrada consiste en la posición de la secuencia, por ejemplo en la posición 9 esta el Fibonacci 34. Lo que se quiere es que de una de las siguiente respuestas, para los los Fibonacci del 0 al 50 inclusive:
#    La entrada consiste en la posición de la secuencia, por ejemplo en la posición 9 esta el
#    34. Lo que se quiere es que de una de las siguiente respuestas, para los los
#    del 0 al 50 inclusive:
#    No es primo
#    Es primo
#    Para los Fibonacci 51 hasta el 1000
#    Para los
#    51 hasta el 1000
#    Probablemente sea primo
#   Entrada
#    La entrada consiste de múltiples casos de prueba y termina cuando no hay más datos. Cada caso de prueba consiste el número de la secuencia que queremos verificar.
#   Salida
#    Por cada caso de entrada imprima en la salida uno de las respuestas solicitadas.
#   Ejemplo Entrada
#    2341011888
#   Ejemplo Salida
#    No es primoEs primoEs primoNo es primoEs primoNo es primo
#   Ayuda

def sieve_of_fibo(n):
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Precompute Fibonacci sequence up to the 1000th term
fibo = sieve_of_fibo(52)

# Precompute primality of each Fibonacci number
prime_status = []
for num in fibo:
    if is_prime(num):
        prime_status.append("Es primo")
    else:
        prime_status.append("No es primo")

# Process input
while True:
    try:
        n = int(input())
        if n < len(prime_status):
            print(prime_status[n])
        else:
            print("Probablemente sea primo")
    except EOFError:
        break