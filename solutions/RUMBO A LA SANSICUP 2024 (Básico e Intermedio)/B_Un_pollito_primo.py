N=int(input())
S=0
for i in range(5,0, -1):
     S+=N//i
     N=N%(i)

print(S)