R, C, K = map(int, input().split())

for _ in range(R):
    x, y = input().split()
    if "-" in x and "*" in y:
        print("N")
        exit()

print("Y")