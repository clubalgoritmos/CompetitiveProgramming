MOD = 998244353

def f(N, K):
    if K == 1:
        return 1
    
    if N <= 2000:
        dp_sum = [dict() for _ in range(N + 1)]
        
        for a1 in range(1, K + 1):
            dp_sum[1][a1] = dp_sum[1].get(a1, 0) + 1
        
        for i in range(2, N + 1):
            for prev_sum, count in dp_sum[i-1].items():
                if prev_sum % (i - 1) != 0:
                    continue
                
                for a in range(1, K + 1):
                    new_sum = prev_sum + a
                    if new_sum % i == 0:
                        dp_sum[i][new_sum] = (dp_sum[i].get(new_sum, 0) + count) % MOD
        
        result = sum(dp_sum[N].values()) % MOD
        return result
    
    return 0

N, K = map(int, input().split())
print(f(N, K))