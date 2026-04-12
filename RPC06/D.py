MOD = 10**9 + 7

def cp(N):
    if N == 1:
        return 0
    
    mx_d = 9 * N
    prev_dp = [0] * (2 * mx_d + 1)
    curr_dp = [0] * (2 * mx_d + 1)
    prev_dp[mx_d] = 1
    
    for n in range(1, N + 1):
        for s in range(-mx_d, mx_d + 1):
            base = prev_dp[s + mx_d]
            if base > 0:
                for da in range(10):
                    for db in range(10):
                        if da != db:
                            if n == 1 and (da == 0 or db == 0):
                                continue
                            ns = s + da - db
                            if -mx_d <= ns <= mx_d:
                                curr_dp[ns + mx_d] += base
                                if curr_dp[ns + mx_d] >= MOD:
                                    curr_dp[ns + mx_d] -= MOD
        prev_dp, curr_dp = curr_dp, [0] * (2 * mx_d + 1)
    
    return prev_dp[mx_d]

Q = int(input())
for _ in range(Q):
    N = int(input())
    print(cp(N))