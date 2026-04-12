import math

def solve(N, A):
    total = sum(A)
    prob = [a / total for a in A]
    dp = [0.0] * (N + 1)
    lcm = [0] * (N + 1)
    for i in range(1, N + 1):
        lcm[i] = i
    for i in range(N, 0, -1):
        dp[i] = 1.0 + sum(prob[j] * dp[lcm[j]] for j in range(i, min(N + 1, len(prob)))) / (1.0 - prob[0])
        if i > 1:
            for j in range(2 * i, N + 1, i):
                lcm[j] = math.gcd(lcm[j], i)
    return dp[1]

N = int(input())
A = list(map(int, input().split()))
print(solve(N, A))