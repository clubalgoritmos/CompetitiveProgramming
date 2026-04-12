n = int(input())
dic = [input().strip() for _ in range(n)]
m = int(input())

dic = set(dic)

for _ in range(m):
    q = input().strip()
    if q in dic:
        print("1")
        continue
    f = False
    for i in range(1, len(q)):
        if q[:i] in dic and q[i:] in dic:
            print("2")
            f = True
            break
    if not f:
        print("0")
