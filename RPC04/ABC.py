def generate_combinations(a, b, c):
    dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
    dp[0][0][0] = 1
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if i > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + (dp[i-1][j][k-1] if k > 0 else 0))
                if j > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + (dp[i][j-1][k-1] if i > 0 else 0))
                if k > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j][k-1] + (dp[i-1][j][k-1] if j > 0 else 0))
    return dp[a][b][c]

i,j,k = map(int,input().split())
if i > j+k or j > i+k or k > i+j:
    print('0')
else:
    print(generate_combinations(i, j, k))