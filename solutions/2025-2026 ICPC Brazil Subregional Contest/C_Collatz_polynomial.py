N = int(input())
ls = set([N - i for i, k in enumerate(input().split()) if k != "0"])
C = 0
while ls != {0}:
    if 0 in ls:
        l1 = set([li + 1 for li in ls])
        l2 = ls - {0}
        ls = l1.symmetric_difference(l2)
    else:
        ls = set([li - 1 for li in ls])
    C += 1
print(C)
