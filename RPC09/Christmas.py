import math

def probability_not_see_caro(r, l):
    if l >= r:
        return 0.0
    return 1 - (2 * l / (2 * math.pi * r))

r, l = map(int, input().split())
print(f"{probability_not_see_caro(r, l):.10f}")