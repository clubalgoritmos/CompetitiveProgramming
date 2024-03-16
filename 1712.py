while True:
    S = input()
    if S=="fin":
        break
    s = 0
    for _ in range(int(S)):
        s+=int(input())
    print(s)