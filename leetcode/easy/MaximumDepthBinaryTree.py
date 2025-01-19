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


def max_depth(root):
    if root is not None:
        # print(root.val)
        left = max_depth(root.left)
        right = max_depth(root.right)
        return max(left, right) + 1
    else:
        return 0


root = build_tree(iter('5 4 3 x x 8 x x 6 x x'.split()), int)
print(max_depth(root))
