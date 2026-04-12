points_1 = list(map(int, input().split()))
points_2 = list(map(int, input().split()))

if sum([point * (i + 1) for i, point in enumerate(points_1)]) > sum(
    [point * (i + 1) for i, point in enumerate(points_2)]
):
    print(1)
elif sum([point * (i + 1) for i, point in enumerate(points_1)]) < sum(
    [point * (i + 1) for i, point in enumerate(points_2)]
):
    print(2)
else:
    print(0)
