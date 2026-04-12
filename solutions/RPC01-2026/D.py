X, Y, S = input().split()
S = int(S)


def base(num_str, base):
    try:
        return all(0 <= int(d) < base for d in num_str)
    except ValueError:
        return False


res = None
for bx in range(2, 11):
    if not base(X, bx):
        continue
    x_val = int(X, bx)
    for by in range(2, 11):
        if not base(Y, by):
            continue
        y_val = int(Y, by)
        if x_val + y_val == S:
            if res is None or (bx < res[0]) or (bx == res[0] and by < res[1]):
                res = (bx, by)

print(res[0], res[1])
