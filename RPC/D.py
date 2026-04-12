import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

N = int(input())
sqrt_N = int(math.sqrt(N))

if N == 1 or is_prime(N) or (sqrt_N * sqrt_N == N and is_prime(sqrt_N)):
    print("N")
else:
    print("Y")