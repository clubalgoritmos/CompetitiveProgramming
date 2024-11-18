#solution
def pos(it, M, mx):
    i = 0
    j = len(it) - 1
    sn = 0
    while i <= j:
        if i == j:
            if it[i] > mx:
                return False
            sn += 1
            i += 1
        elif it[i] + it[j] <= mx:
            sn += 1
            i += 1
            j -= 1
        else:
            if it[i] > mx:
                return False
            sn += 1
            i += 1
    return sn <= M

N, M = map(int, input().split())
it = list(map(int, input().split()))
it.sort(reverse=True)

lw = 0
hg = max(it) * 2
while lw < hg:
    mid = (lw + hg) // 2
    if pos(it, M, mid):
        hg = mid
    else:
        lw = mid + 1

print(lw)