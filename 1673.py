from bisect import bisect_right

dinos = sorted(int(input()) for _ in range(int(input())))
weights = [0] * len(dinos)
counts = [0] * len(dinos)

for i, dino in enumerate(dinos):
    weights[i] = dino if i == 0 else weights[i-1] + dino
    counts[i] = 1 if i == 0 else counts[i-1] + 1

for _ in range(int(input())):
    Q = int(input())
    index = bisect_right(dinos, Q)
    if index:
        print(counts[index-1], weights[index-1])
    else:
        print(0, 0)