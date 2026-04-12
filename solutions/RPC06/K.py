MOD = 10**9 + 7

def modinv(a, m=MOD):
    return pow(a, m-2, m)

def expected_weeks(N, k):
    result = 0
    prob = 1
    for i in range(1, k + 1):
        result = (result + prob * N) % MOD
        prob = (prob * (N - i)) % MOD
        prob = (prob * modinv(N)) % MOD
    return result

N, k = map(int, input().split())
print(expected_weeks(N, k))