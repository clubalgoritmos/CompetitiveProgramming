for _ in range(int(input())):
    S = input().strip()
    vec = []
    for i, si in enumerate(S):
        if si in {"(", "["}:
            vec.append(si)
        elif vec and ((vec[-1] == "(" and si == ")") or (vec[-1] == "[" and si == "]")):
            vec.pop()
        else:
            vec.append(si)
    print("Yes" if not vec else "No")