#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

bool check_acronym(const string& acronym) {
    set<char> vowels = {'A', 'E', 'I', 'O', 'U', 'Y'};
    for (int i = 0; i <= acronym.size() - 3; ++i) {
        if (vowels.count(acronym[i]) || vowels.count(acronym[i+1]) || vowels.count(acronym[i+2])) {
            continue;
        } else {
            return false;
        }
    }
    return true;
}

void generate_acronyms(vector<string>& prefixes, string acronym = "", int i = 0) {
    if (i == prefixes.size()) {
        if (check_acronym(acronym)) {
            cout << acronym.size() << endl;
            exit(0);
        }
        return;
    }
    for (char c : prefixes[i]) {
        generate_acronyms(prefixes, acronym + c, i + 1);
    }
}

int main() {
    int N;
    cin >> N;
    vector<vector<string>> prefixes(N);
    for (int i = 0; i < N; ++i) {
        string word;
        cin >> word;
        for (int j = 1; j <= min(3, (int)word.size()); ++j) {
            prefixes[i].push_back(word.substr(0, j));
        }
    }
    generate_acronyms(prefixes);
    cout << '*' << endl;
    return 0;
}