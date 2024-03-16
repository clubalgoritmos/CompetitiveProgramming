import math
while True:
    try:
        a,n = map(int,input().split())
        print(math.floor(math.log(n,a)))
    except EOFError:x
        break