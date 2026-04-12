#Time limit
def can_distribute_equally(bags):
    alice_candies = 0
    bob_candies = 0
    for candies in bags:
        if alice_candies <= bob_candies:
            alice_candies += candies
        else:
            bob_candies += candies
    #print(*bags)
    return alice_candies == bob_candies

def backtrack(bags, index):
    if index == len(bags):
        return can_distribute_equally(bags)
    
    for i in range(index, len(bags)):
        bags[index], bags[i] = bags[i], bags[index]
        if backtrack(bags, index + 1):
            return True
        bags[index], bags[i] = bags[i], bags[index]
    
    return False

N = int(input())
a = list(map(int, input().split()))

if backtrack(a, 0):
    print(*a)
else:
    print(-1)