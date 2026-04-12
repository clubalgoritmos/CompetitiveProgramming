def area(points):
    return abs(sum(points[i-1][0]*points[i][1] - points[i][0]*points[i-1][1] for i in range(len(points))) / 2)

def solve(points):
    n = len(points)
    points = points + points
    j = 1
    min_diff = float('inf')
    min_cut = None
    total_area = area(points[:n])
    for i in range(n):
        while area(points[i:j+1]) <= total_area / 2:
            j += 1
        for k in range(j-1, j+1):
            diff = abs(total_area - 2 * area(points[i:k+1]))
            if diff < min_diff:
                min_diff = diff
                min_cut = (i, k % n)
    return min_cut
n = input()
print(solve([tuple(map(int, input().split())) for _ in range(int(n))]))