x=int(input())
if x%2==0:
    print("No es Número Primo")
else:
    if len(str(x))==1:
        ylist = [int(y) for y in list(str(x*x))]
    else:
        ylist = [int(y) for y in list(str(x))]
    y = 0
    while sum(ylist) !=1:
        rel = (ylist[0]*ylist[0]) + (ylist[1]*ylist[1])
        ylist = [int(y) for y in list(str(rel))]
        y = y+1
        if y > 10:
            print("Número Primo Infeliz")
            break
           
    if sum(ylist) == 1:
        print("Número Primo Feliz")