#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, T;
    cin >> N >> T;

    vector<int> tiempos(N);
    for (int i = 0; i < N; ++i) {
        cin >> tiempos[i];
    }

    int mitad = N / 2;
    vector<int> grupo1(tiempos.begin(), tiempos.begin() + mitad);
    vector<int> grupo2(tiempos.begin() + mitad, tiempos.end());

    vector<int> suma_grupo1, suma_grupo2;

    int n1 = grupo1.size();
    for (int mask = 0; mask < (1 << n1); ++mask) {
        int suma = 0;
        for (int i = 0; i < n1; ++i) {
            if (mask & (1 << i)) {
                suma += grupo1[i];
            }
        }
        if (suma <= T)
            suma_grupo1.push_back(suma);
    }


    int n2 = grupo2.size();
    for (int mask = 0; mask < (1 << n2); ++mask) {
        int suma = 0;
        for (int i = 0; i < n2; ++i) {
            if (mask & (1 << i)) {
                suma += grupo2[i];
            }
        }
        if (suma <= T)
            suma_grupo2.push_back(suma);
    }

    sort(suma_grupo2.begin(), suma_grupo2.end());

    int mejor = 0;
    for (int s1 : suma_grupo1) {
        int restante = T - s1;
        auto it = upper_bound(suma_grupo2.begin(), suma_grupo2.end(), restante);
        if (it != suma_grupo2.begin()) {
            --it;
            int candidato = s1 + *it;
            if (candidato > mejor)
                mejor = candidato;
        }
    }

    cout << mejor << endl;
    return 0;
}