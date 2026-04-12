#solucion
from collections import Counter
N = int(input())
ls = sorted(map(int,input().split()),reverse=True)
if all(v%3==0 for k, v in Counter(ls).items()):
    print("N")
    exit()
print("Y")