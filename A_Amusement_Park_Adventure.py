#Solucion
N, H = map(int, input().split())
print(len([y for x in input().split() if (y:=int(x))<=H]))