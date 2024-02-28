a,b,c = map(int, input().split())
c+=1
if c==60:
    c=0
    b+=1
    if b==60:
        b=0
        a+=1
        if a==24:
            a=0
print("{:02d}:{:02d}:{:02d}".format(a, b, c))