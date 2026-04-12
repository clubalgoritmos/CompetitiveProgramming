a = list(map(int, input().split()))
result = 1
for x in a:
    result *= x + 1
print(result - 1)
