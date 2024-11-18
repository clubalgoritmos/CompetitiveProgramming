N, S = map(int,input().split())
T = list(map(int,input().split()))
last = T[0]
c=1
for i in range(1,N):
     if abs(last-T[i])>=S:
          c+=1
          last=T[i]
print(c)