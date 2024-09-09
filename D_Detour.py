#time limit
from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(edges, start_node, end_node):
    graph = defaultdict(list)
    for left, right, cost in edges:
        graph[left].append((cost, right))
        graph[right].append((cost, left))
    priority_queue = [(0, start_node, ())]
    visited = set()

    while priority_queue:
        current_cost, current_node, path = heappop(priority_queue)
        if current_node in visited:
            continue
        visited.add(current_node)
        path = (current_node, path)
        if current_node == end_node:
            return current_cost
        for cost, neighbor in graph.get(current_node, ()):
            if neighbor not in visited:
                heappush(priority_queue, (current_cost + cost, neighbor, path))
    return "-1"

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
for i in range(len(edges)):
    edges_without_i = edges[:i] + edges[i+1:]
    result = dijkstra(edges_without_i, edges[i][0], edges[i][1])
    print(result)
