S,N = input().split()
N = int(N) % len(S)
if N == 0:
    print(S)
else:
    print(S[-N:] + S[:-N])