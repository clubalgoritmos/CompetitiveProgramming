/* https://jv.umsa.bo/oj/problem.php?id=1091
  Divisibilidad
  Enviar
  Estado
  Descripción
    Se le darán dos números naturales a y b. Su tarea es verificar si a es divisible por b ó b s divisible por a.
    Se le darán dos números naturales a y b. Su tarea es verificar si a es divisible por b ó b s divisible por a.
    Se le darán dos números naturales a y b. Su tarea es verificar si a es divisible por b ó b s divisible por a.
   Entrada
    Se le darán muchos casos de prueba.La entrada consta de dos números naturales a y b no ayores a $100$.
    Se le darán muchos casos de prueba.La entrada consta de dos números naturales a y b no ayores a $100$.
    Se le darán muchos casos de prueba.La entrada consta de dos números naturales a y b no ayores a $100$.
   Salida
    Existen tres posibles respuestas.
    Existen tres posibles respuestas.
    Existen tres posibles respuestas.
    Si a es divisible por b imprimir: "a es divisible por b".
    Si a es divisible por b imprimir: "a es divisible por b".
    Si b es divisible por a imprimir: "b es divisible por a".
    Si b es divisible por a imprimir: "b es divisible por a".
    Si ninguno de los casos se da imprimir: "-1".
    Si ninguno de los casos se da imprimir: "-1".
    Si ninguno de los casos se da imprimir: "-1".
    Si ninguno de los casos se da imprimir: "-1".
    Los valores de a y b dependen de la entrada.Imprimir la respuesta en una sola linea.
    Los valores de a y b dependen de la entrada.Imprimir la respuesta en una sola linea.
    Los valores de a y b dependen de la entrada.
    Imprimir la respuesta en una sola linea.
    Imprimir la respuesta en una sola linea.
   Ejemplo Entrada
    5 2552 25 13
   Ejemplo Salida
    25 es divisible por 552 es divisible por 2-1
   Ayuda
*/

#include <iostream>
using namespace std;

int main() {
    int a, b;
    while (cin >> a >> b) {
        if (a % b == 0) {
            cout << a << " es divisible por " << b << endl;
        } else if (b % a == 0) {
            cout << b << " es divisible por " << a << endl;
        } else {
            cout << -1 << endl;
        }
    }
    return 0;
}