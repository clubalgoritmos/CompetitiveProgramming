import math
s, d, m = (int(input(),2) for _ in range(3))

x = math.floor(m/(2)**(d-1))
if math.floor((x+s)/(2)**d)!=0:
    print("Infinite money!")
    exit()

print(s,d,m)
y = x+s
i = 0
while y>0:
    y=y//2
    i+=1
print(i)