import math

def volumen_tronco_cono(l, r, theta):
    h = l * math.cos(theta)
    R = r + l * math.sin(theta)
    return (math.pi * h * (R**2 + R*r + r**2)) / 3

def encontrar_angulo_optimo(l, r):
    lo, hi = 0, math.pi / 2
    # Reducing the number of iterations to a reasonable amount
    # This should be enough to achieve the required precision
    for _ in range(100):  # Adjusted from 100000 to 100
        mid1 = lo + (hi - lo) / 3
        mid2 = hi - (hi - lo) / 3
        if volumen_tronco_cono(l, r, mid1) < volumen_tronco_cono(l, r, mid2):
            lo = mid1
        else:
            hi = mid2
    return (lo + hi) / 2

N = int(input())
for _ in range(N):
    l, r = map(int, input().split())
    angulo_optimo = encontrar_angulo_optimo(l, r)
    # Ensure the output format matches the expected precision
    print(f"{angulo_optimo:.10f}")