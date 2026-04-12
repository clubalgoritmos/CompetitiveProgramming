#include <iostream>
#include <algorithm>

using namespace std;

int countCombinations(int A, int B, int C) {
    int dp[A+1][B+1][C+1][3] = {};

    dp[0][0][0][0] = dp[0][0][0][1] = dp[0][0][0][2] = 1;

    for (int a = 0; a <= A; ++a) {
        for (int b = 0; b <= B; ++b) {
            for (int c = 0; c <= C; ++c) {
                if (a > 0) dp[a][b][c][0] = dp[a-1][b][c][1] + dp[a-1][b][c][2];
                if (b > 0) dp[a][b][c][1] = dp[a][b-1][c][0] + dp[a][b-1][c][2];
                if (c > 0) dp[a][b][c][2] = dp[a][b][c-1][0] + dp[a][b][c-1][1];
            }
        }
    }

    return dp[A][B][C][0] + dp[A][B][C][1] + dp[A][B][C][2];
}

int main() {
    int A, B, C;
    cin >> A >> B >> C;
    cout << countCombinations(A, B, C) << endl;
    return 0;
}