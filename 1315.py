n = int(input())
V = [0]
for x in input().split():
    x = int(x)
    V.append(abs(V[-1]-x))
print(V[1:])