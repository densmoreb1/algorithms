# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
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


def inorder(root):
    res = []

    def dfs(root, res):
        if root is not None:
            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)
        else:
            return None
    dfs(root, res)
    return res


# root = build_tree(iter('5 4 3 x x 8 x x 6 x x'.split()), int)
root = build_tree(iter('1 2 3 4 5 x 8 x x 6 7 9'.split()), int)
print(inorder(root))
