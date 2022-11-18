from collections import deque
from typing import List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

root = build_tree(iter('1 2 4 x 7 x x 5 x x 3 x 6 x x'.split()), int)

# Q1
def level_order_traversal(root: Node):
    q = deque([root])
    res = []

    while q:
        n = len(q)
        level = []
        for _ in range(n):
            node = q.popleft()
            level.append(node.val)
            for child in [node.left, node.right]:
                if child:
                    q.append(child)

        res.append(level)
    return res

# Q2
def zigzag(root: Node):
    q = deque([root])
    res = []
    bool = True

    while q:
        level = []
        n = len(q)
        for _ in range(n):
            node = q.popleft()
            if bool:
                level.append(node.val)
            else:
                level.insert(0, node.val)
            for c in [node.left, node.right]:
                if c:
                    q.append(c)
        res.append(level)
        bool = not bool
    return res

# Q3
def rightmost(root: Node):
    res = []
    q = deque([root])

    while q:
        n = len(q)
        res.append(q[0].val)
        for _ in range(n):
            node = q.popleft()
            for c in [node.left, node.right]:
                if c:
                    q.append(c)
        
    return res
