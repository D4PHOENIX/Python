class TreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []


def mini_max(node, maximizingPlayer):
    if not node.children:  # Base case: leaf node
        return node.value

    if maximizingPlayer:
        bestValue = float('-inf')
        for child in node.children:
            value = mini_max(child, not maximizingPlayer)
            bestValue = max(bestValue, value)
        return bestValue
    else:
        bestValue = float('inf')
        for child in node.children:
            value = mini_max(child, not maximizingPlayer)
            bestValue = min(bestValue, value)
        return bestValue

# Define the tree structure
tree = TreeNode("A", [
    TreeNode("B", [TreeNode("D", [TreeNode(-1), TreeNode(4)]), TreeNode("E", [TreeNode(2), TreeNode(6)])]),
    TreeNode("C", [TreeNode("F", [TreeNode(-3), TreeNode(-5)]), TreeNode("G", [TreeNode(0), TreeNode(7)])])
])

# Call the Mini-max algorithm on the root node
optimalValue = mini_max(tree, True)
print("Optimal value:", optimal_value)
