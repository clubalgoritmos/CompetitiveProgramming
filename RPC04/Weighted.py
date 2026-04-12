from operator import itemgetter

N, S = map(int,input().split())
L = [int(input()) for _ in range(N)]

def window(*args):
    return sum((i+1)*arg for i, arg in enumerate(args))

L = sorted(((i+1, window(*L[i:i+S])) for i in range(N-S+1)), key=itemgetter(1))

for l in L:
    print(*l, sep=' ')