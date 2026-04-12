#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, S;
    cin >> N >> S;
    vector<int> L(N);
    vector<int> prefixSum(N+1, 0);
    for(int i = 0; i < N; i++) {
        cin >> L[i];
        prefixSum[i+1] = prefixSum[i] + L[i];
    }

    vector<pair<int, int>> windows;
    for(int i = 0; i <= N - S; i++) {
        int window_sum = 0;
        for(int j = 0; j < S; j++) {
            window_sum += (j+1) * (prefixSum[i+j+1] - prefixSum[i+j]);
        }
        windows.push_back(make_pair(i+1, window_sum));
    }

    sort(windows.begin(), windows.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.second < b.second;
    });

    for(const auto& window : windows) {
        cout << window.first << " " << window.second << "\n";
    }

    return 0;
}