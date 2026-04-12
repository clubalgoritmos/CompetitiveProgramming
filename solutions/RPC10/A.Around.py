l, r = map(int, input().strip().split())

mul = 1
b = max(l, r)
for i in range(l + r, l + r - b, -1):
    mul *= i
f = 1
for i in range(1, b + 1):
    f *= i

if l > r:
    print(mul // f, (r + l) * (l - r), l, r)
else:
    print(mul // f)
