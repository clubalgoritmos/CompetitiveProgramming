/*# https://jv.umsa.bo/oj/problem.php?cid=2822&pid=0
## https://jv.umsa.bo/oj/problem.php?id=1013
#  Suma igual a XOR
#  Enviar
#  Estado
#  Descripción
#    Un dia Reus aprendio la operacion bit a bit $XOR$ donde los bits en la misma posicion que sean iguales se los ponen en $0$ y los bits en la misma posicion que sean diferentes los ponen en $1$.
#    A Reus se le ocurrio el siguiente problema dado un numero entero $N$ contar los diferentes $x$ que satisfacen las condiciones siguientes.
#    $0 \leq x \leq N$
#    $N + x = N \oplus x$
#    Por ejemplo si $N = 4$ los $x$ que satisfacen ambas condiciones son:
#    $4 + 0 = 4 \oplus 0 = 4$
#    $4 + 1 = 4 \oplus 1 = 5$
#    $4 + 2 = 4 \oplus 2 = 6$
#    $4 + 3 = 4 \oplus 3 = 7$
#    Entonces la respuesta seria 4.
#    Como la cantidad de casos de prueba podria ser muy grande Reus te pide que elabores un programa que resuelva el problema mencionado.
#   Entrada
#    La primera línea contiene el único entero $t$ $(1 \leq t \leq 10^5)$ — el número de casos de prueba.
#    La primera y única línea de cada caso de prueba contiene un entero $N$ $(1 \leq N \leq 10^{15})$ — descrito en el problema.
#   Salida
#    Por cada caso de prueba imprimir la respuesta.
#   Ejemplo Entrada
#    245
#   Ejemplo Salida
#    42
#   Ayuda
#    Para $N = 5$ los $x$ que satisfacen ambas condiciones son:
#    $5 + 0 = 5 \oplus 0 = 5$
#    $5 + 2 = 5 \oplus 2 = 7$ **/

#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        long long N;
        cin >> N;
        long long c = 0;
        while(N > 0) {
            if((N & 1) == 0) {
                c++;
            }
            N >>= 1;
        }
        long long result = 1LL << c;
        cout << result << "\n";
    }
    return 0;
}