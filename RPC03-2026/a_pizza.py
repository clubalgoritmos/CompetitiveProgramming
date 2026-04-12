n = int(input())
ss = 0
ms = 0
ls = 0

for _ in range(n):
    sz, sl = input().split()
    sl = int(sl)
    
    if sz == 'S':
        ss += sl
    elif sz == 'M':
        ms += sl
    else:
        ls += sl

bx = 0
bx += (ss + 5) // 6
bx += (ms + 7) // 8
bx += (ls + 11) // 12

print(bx)