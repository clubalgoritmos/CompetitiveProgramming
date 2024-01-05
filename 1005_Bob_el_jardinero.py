for i in range(int(input())):
    v={'a':0,'e':0,'i':0,'o':0,'u':0}
    sm=0
    for x in input():
        if x in v:
            v[x]+=1
        sm+=1
    print("Caso {}:".format(i+1))
    for k,v in v.items():
        print(f"{k}= {(v/sm)*100:.2f}")