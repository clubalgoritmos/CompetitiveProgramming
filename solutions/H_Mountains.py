#Solucion
mx = float("-inf")
mx_i = 0
t=0
for i, ai in enumerate(input(),1):
    if ai=="+":
        t+=1
    else:
        t-=1
    if t>mx:
        mx=t
        mx_i=i
print(mx_i)