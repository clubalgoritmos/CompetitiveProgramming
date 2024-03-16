for _ in range(int(input())):
    n = input()
    fuc = lambda n: int(n)**2
    while n!="1" and n!="4":
        n = str(sum(list(map(fuc,n))))
    if n!="1":
        print("Triste")
    else:
        print("Feliz")