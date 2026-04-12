#include <iostream>
#include <cmath>

using namespace std;

/* * FUNCIÓN REUTILIZABLE: Raíz cuadrada entera exacta.
 * ¿Por qué no usar sqrt() directamente?
 * Porque el discriminante puede llegar a ~4 * 10^18.
 * El tipo 'double' (usado por sqrt) pierde precisión a partir de 2^53 (~9 * 10^15).
 * Esta función es un salvavidas que te servirá para cualquier proyecto matemático
 * donde manejes enteros de 64 bits al límite.
 */
long long raiz_entera(long long x) {
    if (x < 0)
        return -1;

    unsigned long long ux = x;
    unsigned long long s = sqrt(ux);

    // Ajuste fino para corregir errores de precisión del hardware
    while ((s + 1) * (s + 1) <= ux)
        s++;
    while (s * s > ux)
        s--;

    return s;
}

int main() {
    // Optimización de la entrada/salida para programación competitiva
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long p, q;
    if (!(cin >> p >> q))
        return 0;

    // Iteramos r hasta su límite máximo.
    for (long long r = 1; r <= 1000000; r++) {
        // Coeficientes de la ecuación: p * n^2 - (p + 2qr) * n + 2qr^2 = 0
        long long b = p + 2LL * q * r;

        // Discriminante: b^2 - 4ac
        long long delta = b * b - 8LL * p * q * r * r;

        // Si el discriminante es negativo, las raíces son imaginarias
        if (delta >= 0) {
            long long s = raiz_entera(delta);

            // Verificamos si es un cuadrado perfecto
            if (s * s == delta) {

                // Evaluamos la primera posible raíz de n: (b - raíz(delta)) / 2p
                long long num1 = b - s;
                if (num1 > 0 && num1 % (2LL * p) == 0) {
                    long long n1 = num1 / (2LL * p);
                    if (n1 >= 2LL * r) { // Condición del problema: g >= r implica n >= 2r
                        cout << r << " " << n1 - r << "\n";
                        return 0; // Se pide el r mínimo, apenas lo encontramos terminamos.
                    }
                }

                // Evaluamos la segunda posible raíz de n: (b + raíz(delta)) / 2p
                long long num2 = b + s;
                if (num2 > 0 && num2 % (2LL * p) == 0) {
                    long long n2 = num2 / (2LL * p);
                    if (n2 >= 2LL * r) {
                        cout << r << " " << n2 - r << "\n";
                        return 0;
                    }
                }
            }
        }
    }

    // Si pasamos de 10^6 sin retornar, no hay solución en el límite.
    cout << "impossible\n";
    return 0;
}
