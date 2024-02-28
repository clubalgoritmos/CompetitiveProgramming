s = int(input())
hv = 3600
mv = 60
h = s//hv
s = s%hv
m = s//mv
s = s%mv
print(h,m,s)