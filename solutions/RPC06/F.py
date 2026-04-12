#Solucion
N, P = map(int,input().split())
A = sorted(map(int,input().split()),reverse=True)
for a in A:
    if a<=P:
        print(a)
        break