#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct Node {
    pair<string, int> data;
    Node* left;
    Node* right;

    Node(pair<string, int> d, Node* l = nullptr, Node* r = nullptr)
        : data(d), left(l), right(r) {}
};

pair<string, int> fganador(pair<string, int> a, pair<string, int> b) {
    if (a.second > b.second) {
        return {a.first, a.second - b.second};
    } else if (a.second < b.second) {
        return {b.first, b.second - a.second};
    } else {
        return (a.first < b.first) ? make_pair(a.first, 0) : make_pair(b.first, 0);
    }
}

Node* build_tree(vector<Node*>& leaves) {
    while (leaves.size() > 1) {
        vector<Node*> next_level;
        for (size_t i = 0; i < leaves.size(); i += 2) {
            if (i + 1 < leaves.size()) {
                pair<string, int> ganador = fganador(leaves[i]->data, leaves[i + 1]->data);
                Node* node = new Node(ganador, leaves[i], leaves[i + 1]);
                next_level.push_back(node);
            } else {
                next_level.push_back(leaves[i]);
            }
        }
        leaves = next_level;
    }
    return leaves[0];
}

int main() {
    int N;
    cin >> N;
    vector<Node*> leaves;
    for (int i = 0; i < N; ++i) {
        string s;
        int a;
        cin >> s >> a;
        leaves.push_back(new Node({s, a}));
    }

    Node* root = build_tree(leaves);
    cout << root->data.first << endl;

    if (root->left && root->right) {
        pair<string, int> runner_up;
        if (root->left->data.first == root->data.first) {
            runner_up = root->right->data;
        } else {
            runner_up = root->left->data;
        }
        cout << runner_up.first << endl;
    }

    return 0;
}