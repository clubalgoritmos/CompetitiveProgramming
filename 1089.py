for _ in range(int(input())):
    S = input()
    if len(S)%2==0:
        print("*")
        continue
    print(S[len(S)//2])