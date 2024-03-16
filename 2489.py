import math

def egyptian_fraction(x, y):
    result = []
    while x != 0:
        z = math.ceil(y/x)
        result.append(z)
        x, y = -y % x, y * z
    return result

for _ in range(int(input())):
    x, y = map(int, input().split())
    fractions = egyptian_fraction(x, y)
    print(" ".join(["(1, {})".format(i) for i in fractions]))