import collections

paths = [input().split("/")[1:] for _ in range(int(input()))]

while True:
    last = sum(len(path) for path in paths)
    commonpath = collections.defaultdict(int)
    for path in paths:
        if path:
            commonpath[path[0]] += 1
    commonpath = max(commonpath, key=commonpath.get)
    for i in range(len(paths)):
        if len(paths[i]) > 1 and paths[i][0] == commonpath:
            paths[i].pop(0)
        else:
            paths[i].insert(0,"..")
    if last <= sum(len(path) for path in paths):
        print(last)
        break
