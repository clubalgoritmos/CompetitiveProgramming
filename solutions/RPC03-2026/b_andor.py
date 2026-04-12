class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def is_leaf(self):
        return self.value in ["T", "F"]

    def is_true(self):
        return self.value == "T"


class Tree:
    def __init__(self, levels, is_and_root):
        self.levels = levels
        self.is_and_root = is_and_root
        self.n = len(levels)

    def build(self):
        if self.n == 0 or not self.levels[0]:
            return None

        nodes_by_level = [[Node(value) for value in level] for level in self.levels]

        for level_idx in range(self.n - 1):
            next_nodes = nodes_by_level[level_idx + 1]
            next_ptr = 0

            for node in nodes_by_level[level_idx]:
                if node.is_leaf():
                    continue

                num_children = int(node.value)
                node.children = next_nodes[next_ptr : next_ptr + num_children]
                next_ptr += num_children

        return nodes_by_level[0][0]

    def evaluate(self, node, level_idx):
        if node.is_leaf():
            return node.is_true()

        is_and = (level_idx % 2 == 0) == self.is_and_root
        child_values = [self.evaluate(child, level_idx + 1) for child in node.children]

        return all(child_values) if is_and else any(child_values)

    def calculate_costs(self, node, level_idx):
        if node.is_leaf():
            return (0, 1) if node.is_true() else (1, 0)

        is_and = (level_idx % 2 == 0) == self.is_and_root
        child_costs = [self.calculate_costs(child, level_idx + 1) for child in node.children]
        free_cost = [min(t_cost, f_cost) for t_cost, f_cost in child_costs]

        if is_and:
            true_cost = sum(cost[0] for cost in child_costs)
            false_cost = (
                min(
                    child_costs[j][1] + sum(free_cost[i] for i in range(len(child_costs)) if i != j)
                    for j in range(len(child_costs))
                )
                if child_costs
                else 0
            )
        else:
            true_cost = (
                min(
                    child_costs[j][0] + sum(free_cost[i] for i in range(len(child_costs)) if i != j)
                    for j in range(len(child_costs))
                )
                if child_costs
                else 0
            )
            false_cost = sum(cost[1] for cost in child_costs)

        return (true_cost, false_cost)


n, t = input().split()
n = int(n)
t = t == "A"

levels = [input().split() for _ in range(n)]
tree = Tree(levels, t)
root = tree.build()

true_cost, false_cost = tree.calculate_costs(root, 0)
print(max(true_cost, false_cost))
