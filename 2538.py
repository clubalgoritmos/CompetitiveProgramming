from math import ceil
n, m, a = (int(x) for x in input().split(' '))
s = ceil(n/a) * ceil(m/a)
print(s)