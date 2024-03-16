#No funciona
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    i,j = min(a),max(a)
    print(i,j)