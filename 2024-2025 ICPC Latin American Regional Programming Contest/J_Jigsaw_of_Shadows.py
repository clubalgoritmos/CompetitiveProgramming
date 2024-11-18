#solucion
import sys
import math

input = sys.stdin.readline

theta_deg, N = input().split()
theta_deg = float(theta_deg)
N = int(N)
theta_rad = math.radians(theta_deg)
tan_theta = math.tan(theta_rad)

intervals = []
for _ in range(N):
    X_str, H_str = input().split()
    X = float(X_str)
    H = float(H_str)
    L = H / tan_theta
    intervals.append((X, X + L))

intervals.sort()
merged = []
for start, end in intervals:
    if not merged or start > merged[-1][1]:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

total_length = sum(end - start for start, end in merged)
print(total_length)