#include <bits/stdc++.h>
using namespace std;

int w, d;

bool is_valid_var(const string &seq) {
    for (int i = 0; i < (int)seq.length() - 1; i++) {
        if (seq[i] == seq[i + 1]) {
            if (seq[i] != 'B')
                return false;
            if (i + 2 < (int)seq.length() && seq[i + 2] == 'B')
                return false;
        }
    }
    return true;
}

bool is_valid_bal(const string &seq) {
    int ca = count(seq.begin(), seq.end(), 'A');
    int cb = count(seq.begin(), seq.end(), 'B');
    int cc = count(seq.begin(), seq.end(), 'C');
    return abs(ca - cb) <= d && abs(cb - cc) <= d && abs(ca - cc) <= d;
}

bool is_valid_pal(const string &seq) {
    return seq != string(seq.rbegin(), seq.rend());
}

long long bt(string seq) {
    if (!is_valid_var(seq))
        return 0;

    if ((int)seq.length() == w) {
        if (is_valid_bal(seq) && is_valid_pal(seq))
            return 1;
        return 0;
    }

    long long cnt = 0;
    for (char ch : {'A', 'B', 'C'}) {
        cnt += bt(seq + ch);
    }

    return cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> w >> d;
    cout << bt("") << endl;

    return 0;
}
