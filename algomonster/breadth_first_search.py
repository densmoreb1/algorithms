"""
When to use BFS over DFS:
    Find nodes close to the root

Data structure:
    Queue pop and popleft

Basic algorithm:
    def bfs_by_queue(root):
        queue = deque([root]) # at least one element in the queue to kick start bfs
        while len(queue) > 0: # as long as there is an element in the queue
            node = queue.popleft() # dequeue
            for child in node.children: # enqueue children
                if OK(child): # early return if problem condition met
                    return FOUND(child)
                queue.append(child)
        return NOT_FOUND
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


def level_order_traversal(root):
    queue = []
    queue.append(root)
    levels = []

    while len(queue) > 0:
        n = len(queue)
        level = []
        for i in range(n):
            node = queue.pop(0)
            level.append(node.val)
            for child in [node.left, node.right]:
                if child is not None:
                    queue.append(child)

        levels.append(level)

    return levels


root = build_tree(iter('1 2 4 x 7 x x 5 x x 3 x 6 x x'.split()), int)
print(level_order_traversal(root))
