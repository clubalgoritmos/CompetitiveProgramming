#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int N;
    cin >> N;
    int last;
    cin >> last;
    vector<int> C;
    C.push_back(last);
    for (int i = 0; i < N - 1; ++i)
    {
        int a;
        cin >> a;
        a += last;
        C.push_back(a);
        last = a;
    }
    int Q;
    cin >> Q;
    for (int i = 0; i < Q; ++i)
    {
        string a;
        int b, c;
        cin >> a >> b >> c;
        if (a == "R")
        {
            if (b == 1)
            {
                cout << C[c - 1] << endl;
            }
            else
            {
                cout << C[c - 1] - C[b - 2] << endl;
            }
        }
        if (a == "U")
        {
            for (int j = b - 1; j < N; ++j)
            {
                C[j] += c;
            }
        }
    }
    return 0;
}