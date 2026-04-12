import math

p_input, q = map(int, input().split())

found = False
for r in range(1, 10**6 + 1):
    a = p_input
    b = -(p_input + 2 * r * q)
    c = 2 * r * r * q

    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        continue

    sqrt_disc = math.isqrt(discriminant)
    if sqrt_disc * sqrt_disc != discriminant:
        continue

    s1 = (-b + sqrt_disc) // (2 * a)
    s2 = (-b - sqrt_disc) // (2 * a)

    for s in [s1, s2]:
        if s > 0:
            g = s - r
            if g >= r and 2 * r * g * q == p_input * (r + g) * (r + g - 1):
                print(r, g)
                found = True
                break

    if found:
        break

if not found:
    print("impossible")
