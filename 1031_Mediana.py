# https://jv.umsa.bo/oj/problem.php?id=1031
#  Mediana
#  Enviar
#  Estado
#  Descripción
#    En un conjunto de números distintos la mediana es un elemento $M$ de tal forma que el numero de elementos mayores a $M$ son exactamente igual al numero de elemento menores a $M$.
#    En un conjunto de números distintos la mediana es un elemento $M$ de tal forma que el numero de elementos mayores a $M$ son exactamente igual al numero de elemento menores a $M$.
#    En un conjunto de números distintos la mediana es un elemento $M$ de tal forma que el numero de elementos mayores a $M$ son exactamente igual al numero de elemento menores a $M$.
#    Por ejemplo dato el conjunto {$1$, $4$, $2$, $5$, $7$} la mediana es $4$ porque hay dos elementos el $7$ y el $5$ que son mayores a $4$ y dos elementos el $1$ y el $2$ menores a $4$.
#    Por ejemplo dato el conjunto {$1$, $4$, $2$, $5$, $7$} la mediana es $4$ porque hay dos elementos el $7$ y el $5$ que son mayores a $4$ y dos elementos el $1$ y el $2$ menores a $4$.
#    Por ejemplo dato el conjunto {$1$, $4$, $2$, $5$, $7$} la mediana es $4$ porque hay dos elementos el $7$ y el $5$ que son mayores a $4$ y dos elementos el $1$ y el $2$ menores a $4$.
#    El conjunto {$1$, $5$, $8$, $3$} no tiene mediana porque ningún elemento satisface la definición anterior.
#    El conjunto {$1$, $5$, $8$, $3$} no tiene mediana porque ningún elemento satisface la definición anterior.
#    El conjunto {$1$, $5$, $8$, $3$} no tiene mediana porque ningún elemento satisface la definición anterior.
#   Entrada
#    La entrada consiste en multiples casos de prueba(Como máximo $100$). En cada caso de prueba vienen en dos líneas. La primera línea contiene un número $n$ ($1$ <= $n$ <= $1000$), el número de elementos del conjunto. La segunda linea contiene $n$ números enteros($a$0, $a$1$a$2,..., $a$n-1) separados por un espacio($1$ <= $a$i<= $1000$). La entrada termina cuando no hay más datos.
#    La entrada consiste en multiples casos de prueba(Como máximo $100$). En cada caso de prueba vienen en dos líneas. La primera línea contiene un número $n$ ($1$ <= $n$ <= $1000$), el número de elementos del conjunto. La segunda linea contiene $n$ números enteros($a$0, $a$1$a$2,..., $a$n-1) separados por un espacio($1$ <= $a$i<= $1000$). La entrada termina cuando no hay más datos.
#    La entrada consiste en multiples casos de prueba(Como máximo $100$). En cada caso de prueba vienen en dos líneas. La primera línea contiene un número $n$ ($1$ <= $n$ <= $1000$), el número de elementos del conjunto. La segunda linea contiene $n$ números enteros($a$0, $a$1$a$2,..., $a$n-1) separados por un espacio($1$ <= $a$i<= $1000$). La entrada termina cuando no hay más datos.
#   Salida
#    Por cada caso de prueba escriba en una linea la mediana del conjunto si existe o $-1$ si no existe.
#    Por cada caso de prueba escriba en una linea la mediana del conjunto si existe o $-1$ si no existe.
#    Por cada caso de prueba escriba en una linea la mediana del conjunto si existe o $-1$ si no existe.
#   Ejemplo Entrada
#    51 4 2 5 7 41 5 8 3 17 51 2 2 3 452 3 3 3 4
#   Ejemplo Salida
#    4-17-1-1
#   Ayuda
#    Ordenar el vector y tomar el valor del medio $M$ y verificar que el numero de elementos mayores a $M$ son exactamente igual al numero de elementos menores a $M$.
#    Ordenar el vector y tomar el valor del medio $M$ y verificar que el numero de elementos mayores a $M$ son exactamente igual al numero de elementos menores a $M$.
#    Ordenar el vector y tomar el valor del medio $M$ y verificar que el numero de elementos mayores a $M$ son exactamente igual al numero de elementos menores a $M$.
#    En el ultimo caso, la respuesta es $-1$, $3$ es la mediana, los elementos menores deberian ser $2$ y $3$, pero $3$ no es menor a la mediana, y los elementos mayores a la mediana deberían ser $3$ y $4$, pero $3$ no es mayor a la mediana.
#    En el ultimo caso, la respuesta es $-1$, $3$ es la mediana, los elementos menores deberian ser $2$ y $3$, pero $3$ no es menor a la mediana, y los elementos mayores a la mediana deberían ser $3$ y $4$, pero $3$ no es mayor a la mediana.
#    En el ultimo caso, la respuesta es $-1$, $3$ es la mediana, los elementos menores deberian ser $2$ y $3$, pero $3$ no es menor a la mediana, y los elementos mayores a la mediana deberían ser $3$ y $4$, pero $3$ no es mayor a la mediana.

while True:
    try:
        n = int(input())
        a = sorted(map(int,input().split()))
        st = set(a)
        if len(st)%2==0 and :
            print(-1)
            continue
        print(a[n//2])
    except EOFError:
        break