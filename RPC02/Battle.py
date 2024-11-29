from math import *

n = int(input())
c = 0

while n > 1:
    n = ceil(log2(n/2))
    c += 1
    
print(c+2)