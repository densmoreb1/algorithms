"""
When to use DFS:
    Tree
    Combinartorial problems
        How many ways are there to arrange something
        Find all possible combinations
        Find all solutions to a puzzle
    Graph problems
        Find a path
        Find connected nodes
        Detect cycles
"""


class Node:
    # Classic binary tree
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(nodes, f):
    """this function builds a tree from input; you don't have to modify it"""
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


def in_order_traversal(root: Node):
    if root is not None:
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)


def pre_order_traversal(root: Node):
    if root is not None:
        print(root.val)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


def post_order_traversal(root: Node):
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val)


root = build_tree(iter('5 4 3 x x 8 x x 6 x x'.split()), int)
in_order_traversal(root)
print('-' * 75)
pre_order_traversal(root)
