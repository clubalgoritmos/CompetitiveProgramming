def solve(i, j, n, a, dp, c):
    if j == 0:
        return 1
    if i == n:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    ans = solve(i + 1, j, n, a, dp, c)
    c[i][j] = 0
    if j - a[i] >= 0:
        curr = solve(i + 1, j - a[i], n, a, dp, c)
        if curr > ans:
            c[i][j] = 1
            ans = curr
    dp[i][j] = ans
    return ans

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    
    if sum_a % 2 != 0:
        print("-1")
        return
    
    dp = [[-1] * (sum_a // 2 + 1) for _ in range(n)]
    c = [[0] * (sum_a // 2 + 1) for _ in range(n)]
    
    ans = solve(0, sum_a // 2, n, a, dp, c)
    if not ans:
        print("-1")
        return
    
    i, j = 0, sum_a // 2
    va, vb = [], []
    while i < n:
        op = c[i][j]
        if op == 1:
            vb.append(a[i])
            j -= a[i]
        else:
            va.append(a[i])
        i += 1
    
    va.sort(reverse=True)
    vb.sort(reverse=True)
    
    suma, sumb = 0, 0
    i, j = 0, 0
    result = []
    for x in range(n):
        if suma <= sumb:
            suma += va[i]
            result.append(va[i])
            i += 1
        else:
            sumb += vb[j]
            result.append(vb[j])
            j += 1
    
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()