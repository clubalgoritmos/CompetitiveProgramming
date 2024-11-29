#include <iostream>
#include <vector>
#include <algorithm> // Para std::sort y std::pair

std::vector<std::pair<int, int>> obtenerSumaConPosicion(const std::vector<int>& lista, int x) {
    std::vector<std::pair<int, int>> sumasConPosicion;
    for (auto it = lista.begin(); it + x <= lista.end(); ++it) {
        int suma = 0;
        for (int i = 0; i < x; ++i) {
            suma += *(it + i) * (i + 1);
        }
        sumasConPosicion.push_back({suma, static_cast<int>(it - lista.begin())});
    }
    return sumasConPosicion;
}

int main() {
    int N, x;
    std::cin >> N >> x;
    std::vector<int> lista(N);
    
    std::vector<std::pair<int, int>> sumasConPosicion = obtenerSumaConPosicion(lista, x);
    // Ordenar las sumas con respecto a sus valores
    std::sort(sumasConPosicion.begin(), sumasConPosicion.end());

    // Imprimir las sumas junto con sus posiciones
    for (const auto& par : sumasConPosicion) {
        std::cout << par.second + 1 << " " << par.first << " " << std::endl;
    }
    std::cout << std::endl;

    return 0;
}