# | competition: "ICPC Pre-National Bolivia – 2024"
# | problem_id: "E"
# | title: "Great Product"


def rec(N):
    if N == 1:
        return []
    for i in range(2, N + 1):
        if N % i == 0:
            break
    return [i] + rec(int(N // i))


while True:
    try:
        print(*rec(int(input())), sep="x")
    except EOFError:
        break
