N = int(input())
c = 0
ls = 0
for i in map(int, input().split()):
    if i > ls:
        ls = i
        c += 1

print(c)
