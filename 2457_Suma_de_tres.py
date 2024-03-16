# https://jv.umsa.bo/oj/problem.php?id=2457
#  Suma de tres
#  Enviar
#  Estado
#  Descripción
#    Te dan tres números enteros $a$, $b$ y $c$. Determina si uno de ellos es la suma de los otros dos.
#    Te dan tres números enteros $a$, $b$ y $c$. Determina si uno de ellos es la suma de los otros dos.
#    Te dan tres números enteros $a$, $b$ y $c$. Determina si uno de ellos es la suma de los otros dos.
#   Entrada
#    La primera línea contiene un solo entero $t$ ($1 \leq t \leq 10000$) — el número de casos de prueba.
#    La primera línea contiene un solo entero $t$ ($1 \leq t \leq 10000$) — el número de casos de prueba.
#    La primera línea contiene un solo entero $t$ ($1 \leq t \leq 10000$) — el número de casos de prueba.
#    La descripción de cada caso de prueba consta de tres números enteros $a$, $b$, $c$ ($0 \leq a,b,c \leq 100$).
#    La descripción de cada caso de prueba consta de tres números enteros $a$, $b$, $c$ ($0 \leq a,b,c \leq 100$).
#    La descripción de cada caso de prueba consta de tres números enteros $a$, $b$, $c$ ($0 \leq a,b,c \leq 100$).
#   Salida
#    Para cada caso de prueba, emita "SÍ" si uno de los números es la suma de los otros dos, y "NO" en caso contrario.
#    Para cada caso de prueba, emita "SÍ" si uno de los números es la suma de los otros dos, y "NO" en caso contrario.
#    Para cada caso de prueba, emita "SÍ" si uno de los números es la suma de los otros dos, y "NO" en caso contrario.
#   Ejemplo Entrada
#    71 4 32 5 89 11 200 0 020 20 204 12 315 7 8
#   Ejemplo Salida
#    SINOSISINONOSI
#   Ayuda
#    En el primer caso de prueba, $1+3=4$.
#    En el primer caso de prueba, $1+3=4$.
#    En el primer caso de prueba, $1+3=4$.
#    En el segundo caso de prueba, ninguno de los números es la suma de los otros dos.
#    En el segundo caso de prueba, ninguno de los números es la suma de los otros dos.
#    En el segundo caso de prueba, ninguno de los números es la suma de los otros dos.
#    En el tercer caso de prueba, $9+11=20$.
#    En el tercer caso de prueba, $9+11=20$.
#    En el tercer caso de prueba, $9+11=20$.

t = int(input())
for i in range(t):
 a,b,c = (int(x) for x in input().split())
 if a==b+c or b==a+c or c==a+b:
  print('SI')
 else:
  print('NO')