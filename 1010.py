S0 = {
    "U":1,
    "M":1,
    "S":1,
    "A":1,
    "I":1,
    "C":2,
    "P":1
}
for _ in range(int(input())):
    S = input()
    for k,v in S0.items():
        if S.count(k)<v:
            print("NO ES POSIBLE")
            break
    else:
        print("ES POSIBLE")
    
