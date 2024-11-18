import math

def max_area(n):
    max_area = 0
    step = 0.0000000001
    h = step
    while h < n:
        low, high = step, n
        while high - low > step:
            w = (low + high) / 2
            total_length = 2 * h + 3 * w + 2 * math.sqrt(h**2 + w**2)
            if total_length <= n:
                low = w
            else:
                high = w
        w = low
        total_length = 2 * h + 3 * w + 2 * math.sqrt(h**2 + w**2)
        if total_length <= n:
            area = 1.5 * h * w
            if area > max_area:
                max_area = area
                print(max_area)
        h += step
    return max_area

n = int(input())
print(f"{max_area(n):.10f}")