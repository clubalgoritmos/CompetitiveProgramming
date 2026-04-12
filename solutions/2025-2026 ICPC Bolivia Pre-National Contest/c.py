N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if all(A[2 * i] == A[2 * i + 1] for i in range(0, N // 2 - 1)) and all(
    B[2 * i] == B[2 * i + 1] for i in range(0, N // 2 - 1)
):
    print("SI")
else:
    print("NO")
