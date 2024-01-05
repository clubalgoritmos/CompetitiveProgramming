def collatz(n):
    pasos = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        pasos += 1
    return pasos

for _ in range(int(input())): # pylint: disable=unused-variable
    print(collatz(int(input())))
"""
for i in range(int(input())):
    x = int(input())
    y = 0
    while x !=1:
        if not (x % 2) == 0:
            x = (3*x + 1)
        else:
            x = round(x/2)
        y = y+1
    print(y)
"""