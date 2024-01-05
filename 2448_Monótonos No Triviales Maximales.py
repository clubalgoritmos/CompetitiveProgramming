secuence = list(input())
secuence.insert(0, "a")
secuence.append("a")
y = 0
for ab in range(1, len(secuence)-1):
    if secuence[ab] == "a" and (secuence[ab-1] == "a" or secuence[ab+1] == "a"):
        y = y+1
print(y)