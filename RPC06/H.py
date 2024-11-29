n, r, c = map(int, input().split())
cd = list(range(1, n + 1))
h = []
s1 = 0
s2 = n - 1

while len(cd) > 2:
    s1 = (s1 + r - 1) % len(cd)
    s2 = (s2 - c + 1) % len(cd)
    if s1 == s2:
        h.append(cd.pop(s1))
        s2 = (s2 - 1) % len(cd) if len(cd) > 0 else 0
    else:
        if s1 < s2:
            cd.pop(s2)
            cd.pop(s1)
            s2 -= 2
        else:
            cd.pop(s1)
            cd.pop(s2)
    if s1 >= len(cd):
        s1 = 0
    if s2 < 0:
        s2 = len(cd) - 1 if len(cd) > 0 else 0

h += cd
h.sort()
print(*h)