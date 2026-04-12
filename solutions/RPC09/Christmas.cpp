#include <iostream>
#include <iomanip>
#include <cmath>

double probability_not_see_caro(int r, int l) {
    if (l >= r) {
        return 0.0;
    }
    return 1 - (2.0 * l / (2.0 * M_PI * r));
}

int main() {
    int r, l;
    std::cin >> r >> l;
    std::cout << std::fixed << std::setprecision(10) << probability_not_see_caro(r, l) << std::endl;
    return 0;
}