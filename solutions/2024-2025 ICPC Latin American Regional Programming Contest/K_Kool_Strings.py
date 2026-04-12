#solution
K, S = input().split()
K = int(K)
S = list(S)
N = len(S)
F = 0
change = lambda x: "1" if x == "0" else "0"

if K == 2:
    A = "01" * (N // 2) + ("0" if N % 2 != 0 else "")
    B = "10" * (N // 2) + ("1" if N % 2 != 0 else "")
    count_A = sum(1 for a, s in zip(A, S) if a != s)
    count_B = sum(1 for b, s in zip(B, S) if b != s)
    if count_A < count_B:
        print(count_A, A)
        exit()
    print(count_B, B)
    exit()

# timelimit
# for i in range(N - K + 1): 
#    char = list(set(S[i : i + K]))
#    if len(char) <= 1:
#        if (i + K < N and S[i + K] == char[0]) or i + K >= N:
#            S[i + K - 1] = change(i + K - 1)
#            F += 1
#            continue
#        S[i + K - 2] = change(i + K - 2)
#        F += 1

fs = S[0]
w = 0
c = 1
ls = []
rs = []
sd = change(fs)

for i in range(1, N):
    if S[i - 1] == S[i]:
        c += 1
    else:
        if c >= K:
            w += c // K
            ls.append((c // K) * [K - 1, 1] + [c % K] if c % K != 0 else (c // K - 1) * [K - 1, 1] + [K - 2, 1, 1])
        else:
            ls.append([c])
        c = 1

if c >= K:
    w += c // K
    ls.append((c // K) * [K - 1, 1] + [c % K] if c % K != 0 else (c // K - 1) * [K - 1, 1] + [K - 2, 1, 1])
else:
    ls.append([c])

for i, sublist in enumerate(ls):
    for j, li in enumerate(sublist):
        rs.append(fs * li if (i+j) % 2 == 0 else sd * li)
#print(ls)
print(w, ''.join(rs))