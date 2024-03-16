A = list(map(int,input().split()))
B = list(map(int,input().split()))
c = 5
if all([(a+b) == c for a,b in zip(A,B)]):
    print("Esta es la llave")
else:
    print("Intenta con otra")