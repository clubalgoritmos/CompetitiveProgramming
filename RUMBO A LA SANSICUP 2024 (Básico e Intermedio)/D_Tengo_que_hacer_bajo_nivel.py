n, T = map(int, input().split())
A = list(map(int, input().split()))
c = 0
s = 0

for ai in A:
    if s + ai > T:
        break
    s += ai
    c += 1

print(c)