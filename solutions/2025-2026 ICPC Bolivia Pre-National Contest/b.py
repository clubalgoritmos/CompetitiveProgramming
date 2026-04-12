S = input().strip()
T = int(input())
vertical = {"A", "H", "I", "M", "O", "T", "U", "V", "W", "X", "Y"}
horizontal = {"B", "C", "D", "E", "H", "I", "K", "O", "X"}

n = len(S)
prefix_v = [0] * n
prefix_h = [0] * n
prefix_v[0] = 1 if S[0] in vertical else 0
prefix_h[0] = 1 if S[0] in horizontal else 0

for i in range(1, n):
    prefix_v[i] = prefix_v[i - 1] + (1 if S[i] in vertical else 0)
    prefix_h[i] = prefix_h[i - 1] + (1 if S[i] in horizontal else 0)

for _ in range(T):
    x, y = map(int, input().split())
    if x == 0:
        ver = prefix_v[y]
        hor = prefix_h[y]
    else:
        ver = prefix_v[y] - prefix_v[x - 1]
        hor = prefix_h[y] - prefix_h[x - 1]

    if ver > hor:
        print("Más simetría vertical.")
    elif hor > ver:
        print("Más simetría horizontal.")
    else:
        print("Simetría igual.")
