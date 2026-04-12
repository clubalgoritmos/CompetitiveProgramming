#Solucion
Q = int(input())
for _ in range(Q):
    N, T = map(int, input().split())
    min_t = T - 1
    count = 0
    for i in range(1, int(min_t**0.5) + 1):
        if min_t % i == 0:
            if i <= N:
                count += 1
            if i != min_t // i and min_t // i <= N:
                count += 1
    print(N if count==0 else count)