p = int(input())
l = int(p / 240)
p = p % 240
c = int(p / 12)
p = p % 12
print((l, c, p))
