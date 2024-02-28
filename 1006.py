for _ in range(int(input())):
    S = input()
    a = True
    for i, Si in enumerate(S):
        if not Si.isalpha():
            print(Si, end="")
            continue    
        if a:
            print(Si.upper(), end="")
            a = False
        else:
            print(Si, end="")
            a=True
    print()