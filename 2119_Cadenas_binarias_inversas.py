# https://jv.umsa.bo/oj/problem.php?cid=2819&pid=8
## https://jv.umsa.bo/oj/problem.php?id=2119
#  Cadenas binarias inversas
#  Enviar
#  Estado
#  Descripción
#    Se le da una cadena $s$ de longitud uniforme $n$. La cadena $s$ es binaria, en otras palabras, consta solo de $0$ y $1$.
#    La cadena $s$ tiene exactamente $\frac{n}{2}$ ceros y$\frac{n}{2}$unos ($n$ es par).
#    La cadena $s$ tiene exactamente $\frac{n}{2}$ ceros y
#    $\frac{n}{2}$
#    unos ($n$ es par).
#    En una operación puede invertir cualquier subcadena de $s$. Una subcadena de una cadena es una subsecuencia contigua de esa cadena.
#    ¿Cuál es el número mínimo de operaciones que necesita para hacer que la cadena $s$ se alterne? Una cadena se alterna si $s_{i} ≠ s_{i + 1}$ para todo $i$. Hay dos tipos de cadenas alternas en general: $01010101$ ... o $10101010$ ...
#   Entrada
#    La primera línea contiene un solo entero $t$ ($1 \leq t \leq 1000$): el número de casos de prueba.
#    La primera línea de cada caso de prueba contiene un único entero $n$ ($2 \leq n \leq 10^{5}$; $n$ es par): la longitud de la cadena $s$.
#    La segunda línea de cada caso de prueba contiene una cadena binaria s de longitud $n$ ($s_{i} \in {0, 1}$). La cadena s tiene exactamente$\frac{n}{2}$ ceros y $\frac{n}{2}$ unos.
#    Se garantiza que la suma total de n en casos de prueba no exceda $10 ^{5}$.
#   Salida
#    Para cada caso de prueba, imprima el número mínimo de operaciones para hacer que $s$ se alterne.
#   Ejemplo Entrada
#    321081110100040110
#   Ejemplo Salida
#    021
#   Ayuda
#    En el primer caso de prueba, la cadena $10$ ya está alternando.
#    En el segundo caso de prueba, podemos, por ejemplo, realizar las siguientes dos operaciones:
#    $11101000$ → $10101100$;
#    $10101100$ → $10101010$.
#    En el tercer caso de prueba, podemos, por ejemplo, invertir los dos últimos elementos de $s$ y obtener: $0110$ → $0101$.

for _ in range(int(input())):
    N = int(input())
    S = input()
    
    print(sum([S[i]!=S[i%2] for i in range(len(S))]))sad
