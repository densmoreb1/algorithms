class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

root = build_tree(iter("5 4 3 x x 8 x x 6 x x".split()), int)

# Q1
def tree_max_depth(root: Node) -> int:
    def dfs(node):
        if node is None:
            return 0
        
        return max(dfs(node.right), dfs(node.left)) + 1

    if root:
        return dfs(root) - 1
    else:
        return 0

#Q2
