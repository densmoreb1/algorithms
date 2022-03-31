# https://leetcode.com/problems/binary-tree-level-order-traversal/

# use bfs keeping track of a level
import collections
def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    q = collections.deque()
    q.append(root)
    
    final = []
    
    while len(q) > 0:
        
        level = []
        
        for i in range(len(q)):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
                
        if level:
            final.append(level)
    return final