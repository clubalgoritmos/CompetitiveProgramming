F, C = map(int, input().split())
cls = [0] * C
for _ in range(F):
    ls = list(map(int, input().split()))
    for i, li in enumerate(ls):
        if li >= cls[i]:
            cls[i] = li
print(sum(cls))
