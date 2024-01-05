abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
a = list(map(int,''.join([str(abc.index(x)+1) for x in input()])))
n = int(''.join(map(str, a)))
while n>100:
    for i in range(1,len(a)):
        a[i-1] = (a[i-1]+a[i])%10
    a.pop(-1)
    n = int(''.join(map(str, a)))

if n==100:
    print(f"{n} - PAREJA FELIZ")
    exit()
print(f"{n} - PAREJA INFELIZ")