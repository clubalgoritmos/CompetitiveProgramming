for _ in range(int(input())):
    a,b = map(int,input().split())
    def mcd(a,b):
        while b:
            a,b = b,a%b
        return a
    print(mcd(a,b))