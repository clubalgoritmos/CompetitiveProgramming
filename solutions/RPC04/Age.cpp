//solucion
#include <iostream>
using namespace std;
int main(){
    int D, A, K, a, i;
    bool v = false;
    cin >> D >> A >> K;
    for (i = 1; i < 150; i++){
        a = (D - K * i)/A;
        if (a > 0){
        if ((a * A + i * K) == D){
            break;
        }
        }
    }
    if ((a * A + i * K) == D){
            cout << "1" << endl;
    }else cout << "0" << endl;
}