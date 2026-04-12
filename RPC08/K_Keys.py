s = input().strip()
M = False
c = 0
ant = '1'

for ch in s:
    if ch == ' ':
        if ant != ch:
            c += 1
    if ch.isupper():
        if ant.isupper() and ant != ch:
            c += 1
        elif ch.lower() == ant:
            c += 1
        elif M and ant == ' ':
            c += 1
        elif ant != ch:
            c += 2
        M = True
    if ch.islower():
        if ant.isupper() and ch == ant.lower():
            c += 0
        elif ant != ch:
            c += 1
        M = False
    ant = ch

print(c)