from collections import defaultdict


def sensor(p, N):
    return p if p <= N else p - N


def dfs(act, obj, g, usados, cam, N):
    if act == obj:
        return True

    for sig in g[act]:
        s = sensor(sig, N)
        if s not in usados:
            usados.add(s)
            cam.append(sig)

            if dfs(sig, obj, g, usados, cam, N):
                return True

            cam.pop()
            usados.remove(s)

    return False


def solve():
    N, M = map(int, input().split())

    g = defaultdict(list)
    for _ in range(M):
        s, t = map(int, input().split())
        g[s].append(t)

    obj = 2 * N
    usados = {sensor(1, N)}
    cam = [1]

    if dfs(1, obj, g, usados, cam, N):
        print(len(cam))
        print(" ".join(map(str, cam)))
    else:
        print("*")


solve()
