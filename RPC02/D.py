import collections

n, m = map(int,input().split())
M = [list(input()) for _ in range(n)]
for mi in range(m):
    dic = collections.defaultdict(int)
    for ni in range(n):
        dic[M[ni][mi]]+=1
    filterta = list(filter(lambda x: x[1] == max(dic.values()), dic.items()))
    filterta.sort(key=lambda x: x[0])
    print(filterta[0][0],end='')
print()