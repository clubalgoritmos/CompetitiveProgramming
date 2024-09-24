MAXN = 1000006
mod = 1000000007

lpf = [0] * MAXN
mobius = [0] * MAXN
mp = [0] * MAXN
f = [0] * MAXN
resp = [0] * MAXN
pot = [0] * MAXN

def calc_lpf():
    for i in range(2, MAXN):
        if lpf[i] == 0:
            for j in range(i, MAXN, i):
                if lpf[j] == 0:
                    lpf[j] = i

def calc():
    calc_lpf()
    mobius[1] = 1
    for i in range(2, MAXN):
        if lpf[i // lpf[i]] == lpf[i]:
            mobius[i] = 0
        else:
            mobius[i] = -1 * mobius[i // lpf[i]]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    calc()
    
    n = int(data[0])
    index = 1
    for _ in range(n):
        x = int(data[index])
        index += 1
        f[x] += 1
    
    for i in range(2, MAXN):
        for j in range(i, MAXN, i):
            mp[i] += f[j]
    
    for i in range(2, MAXN):
        for j in range(i, MAXN, i):
            resp[j] += (mobius[i] * -1 * mp[i])
    
    pot[0] = 1
    for i in range(1, MAXN):
        pot[i] = (pot[i - 1] * 2) % mod
    
    q = int(data[index])
    index += 1
    results = []
    for _ in range(q):
        x = int(data[index])
        index += 1
        results.append(pot[n - resp[x]])
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()