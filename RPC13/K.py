h, m = map(int, input().split())
print("yes" if (m - 12 * h) % 360 == 0 else "no")