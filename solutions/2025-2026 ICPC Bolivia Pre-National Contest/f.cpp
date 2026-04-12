#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> la(n);
    for (int i = 0; i < n; ++i)
        cin >> la[i];

    multiset<int> prefix, suffix;
    for (int x : la)
        suffix.insert(x);

    vector<long long> output;

    for (int i = 0; i < n - 1; ++i) {
        int x = la[i];
        prefix.insert(x);
        suffix.erase(suffix.find(x));

        int l, r;
        cin >> l >> r;

        long long sum_prefix = 0, sum_suffix = 0;

        if (l > (int)prefix.size()) {
            for (int v : prefix)
                sum_prefix += v;
        } else {
            auto it = prefix.rbegin();
            for (int cnt = 0; cnt < l && it != prefix.rend(); ++cnt, ++it)
                sum_prefix += *it;
        }

        if (r > (int)suffix.size()) {
            for (int v : suffix)
                sum_suffix += v;
        } else {
            auto it = suffix.begin();
            for (int cnt = 0; cnt < r && it != suffix.end(); ++cnt, ++it)
                sum_suffix += *it;
        }

        output.push_back(sum_prefix - sum_suffix);
    }

    for (auto v : output)
        cout << v << '\n';
    return 0;
}
