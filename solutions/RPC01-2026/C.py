teams = int(input())

next_pow2 = 1
while next_pow2 < teams:
    next_pow2 <<= 1

if teams & (teams - 1) == 0:
    print(0)
else:
    print(2 * (teams - (next_pow2 >> 1)))
