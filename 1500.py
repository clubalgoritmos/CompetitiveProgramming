N = input()
A = list(map(int,input().split()))
if A==A[::-1]:
    print("SI")
    exit()
print("NO")