for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        continue
    print(f"{(n-1)**3}+{n**3}")
