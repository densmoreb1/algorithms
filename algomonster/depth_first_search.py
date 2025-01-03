class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x':
        return None
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


# Q2
def visible_tree_node(root):
    def dfs(node, m):
        if node is None:
            return 0

        total = 0
        if node.val >= m:
            total += 1

        total += dfs(node.right, max(m, node.val))
        total += dfs(node.left, max(m, node.val))

        return total

    if root is None:
        return 0

    return dfs(root, -float('inf'))

# Q3


def balanced(root):
    def dfs(node):
        if node is not None:
            return 0

        left_height = dfs(node.left)
        right_height = dfs(node.right)

        if left_height == -1 or right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    height = dfs(root)
    if height == -1:
        return False
    else:
        return True

# Q4


def valid_binary_tree(root: Node):

    b = True

    def dfs(node: Node, min_val, max_val):
        if node is None:
            return True

        if not (min_val < node.val < max_val):
            return False

        return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

    return dfs(root, float('-inf'), float('inf'))


root = build_tree(iter("6 4 3 x x 5 x x 8 x x".split()), int)

print(valid_binary_tree(root))
