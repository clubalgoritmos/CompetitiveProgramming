import math
N,k = map(int,input().split())
print(int(math.log10(N))+1, (N//10**(k-1))%10)