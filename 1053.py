for _ in range(int(input())):
    input()
    graph = {}
    start = input()
    while True:
        try:
            a,b = input()
            if a not in graph:
                graph[a] = set()
            if b not in graph:
                graph[b] = set()
            graph[a].add(b)
            graph[b].add(a)
        except Exception as exp:
            break
    visited = set()
    c=0
    for k in graph:
        if not k in visited:
            c+=1
            visited.add(k)
            stack = [k]
            while stack:
                node = stack.pop()
                for i in graph[node]:
                    if not i in visited:
                        visited.add(i)
                        stack.append(i)
    print(c)
    print()