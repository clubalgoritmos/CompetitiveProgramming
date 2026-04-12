#include <iostream>
#include <vector>
using namespace std;

vector<int> subtree_size;
int max_traversals = 0, count = 0;

int dfs(int node, int parent, const vector<vector<int>>& adj) {
    subtree_size[node] = 1;
    for (int child : adj[node]) {
        if (child != parent) {
            subtree_size[node] += dfs(child, node, adj);
        }
    }
    if (parent != -1) {
        int traversals = subtree_size[node] * (adj.size() - subtree_size[node]);
        if (traversals > max_traversals) {
            max_traversals = traversals;
            count = 1;
        } else if (traversals == max_traversals) {
            count++;
        }
    }
    return subtree_size[node];
}

int main() {
    int N;
    cin >> N;
    vector<vector<int>> adj(N);
    subtree_size.assign(N, 0);
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(0, -1, adj);

    cout << max_traversals << " " << count << endl;

    return 0;
}