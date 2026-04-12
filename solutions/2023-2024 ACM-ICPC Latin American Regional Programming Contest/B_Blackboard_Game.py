# | competition: "ICPC Latin American Regional – 2023"
# | problem_id: "B"
# | title: "Blackboard Game"
# | tags: ["Graph Traversal", "Dynamic Programming", "Greedy"]
# | language: "Python"
# | approach: "Brute Force Simulation"
# | description: "Find the longest subsequence of dishes (1 to R×C) that can be visited in order on a 2D grid, where movement is allowed only to adjacent cells (up, down, left, right). Revisiting cells is allowed but dishes are only counted once."
from collections import Counter

N = int(input())
ls = sorted(map(int, input().split()), reverse=True)
if all(v % 3 == 0 for k, v in Counter(ls).items()):
    print("N")
    exit()
print("Y")
