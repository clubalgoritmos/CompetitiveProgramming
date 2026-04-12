#solucion
def find_cycles(a):
    v = [False] * len(a)
    s = 0
    for i in range(len(a)):
        if not v[i]:
            j = i
            c = 0
            while not v[j]:
                v[j] = True
                j = a[j] - 1
                c += 1
            if c > 0:
                s += c - 1
    return s

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

t = find_cycles(x) + find_cycles(y)
print(t)