from math import atan2, pi

def area(a, b, c):
    return abs((b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])) / 2

def solve(points):
    points.sort(key=lambda p: atan2(p[1], p[0]))
    n = len(points) // 3
    triangles = [points[i::n] for i in range(n)]
    areas = [area(*triangle) for triangle in triangles]
    return round(max(areas) - min(areas), 1)

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(3*n)]
print(solve(points))