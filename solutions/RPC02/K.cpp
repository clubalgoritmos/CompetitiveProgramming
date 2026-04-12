#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> A;
    int n;
    while (cin >> n) {
        A.push_back(n);
    }

    int c = 0;
    vector<int> B = A;
    sort(B.begin(), B.end());

    for (int i = 0; i < A.size(); ++i) {
        if (A[i] != B[i]) {
            for (int j = i + 1; j < A.size(); ++j) {
                if (A[j] == B[i]) {
                    swap(A[i], A[j]);
                    c += j - i;
                    break;
                }
            }
        }
    }

    cout << c << endl;
    return 0;
}