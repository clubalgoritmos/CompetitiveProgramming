#solucion
N = int(input())
A = list(map(int,input().split()))

counter = 1
max_length = 1

for i in range(1, N):
    if A[i] > A[i-1]:
        counter += 1
        max_length = max(max_length, counter)
    else:
        counter = 1

print(max_length)