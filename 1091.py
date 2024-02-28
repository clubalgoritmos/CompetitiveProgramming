import sys
for i in sys.stdin:
    a,b = map(int, i.split())
    if a%b==0:
        print(f"{a} es divisible por {b}")
    elif b%a==0:
        print(f"{b} es divisible por {a}")
    else:
        print(-1)