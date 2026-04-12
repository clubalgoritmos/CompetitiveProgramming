n, x, y = map(int, input().split())

n = n // 2 + 1
print(100 - 10 * (max(abs(n - x), abs(n - y))))
