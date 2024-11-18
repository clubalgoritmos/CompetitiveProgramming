from itertools import permutations

def calculate_cost(switches):
    total_cost = 0
    current_position = 1
    
    for cost, ports in switches:
        total_cost += cost * current_position
        current_position += ports
    
    return total_cost

def min_total_cost(switches):
    min_cost = float('inf')
    
    for perm in permutations(switches):
        cost = calculate_cost(perm)
        if cost < min_cost:
            min_cost = cost
            #print(perm)
    return min_cost

n,m = map(int,input().split())
switches = [tuple(map(int,input().split())) for _ in range(n)]
print(min_total_cost(switches))