from math import gcd, sqrt

simplify = lambda n, d: (n // gcd(n, d), d // gcd(n, d))
integral = lambda A, B, C, x: (A * x**3) / 3 + (B * x**2) / 2 + C * x

t = int(input())
for _ in range(t):
    A, B, C, L, R = map(int, input().split())
    D = B**2 - 4*A*C
    r = []
    if D >= 0:
        r1, r2 = (-B - sqrt(D)) / (2*A), (-B + sqrt(D)) / (2*A)
        r = [x for x in [r1, r2] if L <= x <= R]
        r.sort()
    
    p = [L] + r + [R]
    total = 0
    for i in range(len(p) - 1):
        total += abs(integral(A, B, C, p[i+1]) - integral(A, B, C, p[i]))
    
    total = round(total * 6)
    n, d = simplify(total, 6)
    print(f"{n}/{d}")