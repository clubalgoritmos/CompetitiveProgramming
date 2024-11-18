N, P = map(int, input().split())

K = N // P

if K % 2 == 0 and N - K * P != 0:
    K -= 1

print(N - K * P)
