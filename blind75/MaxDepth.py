# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# use dfs to find the bottom

def maxDepth(root) -> int:

    def dfs(node):
        right = 1
        left = 1
        
        if node == None:
            return 0
        
        if node.right == None and node.left == None:
            return 1
        else:
            if node.right != None:
                right = dfs(node.right) + 1

            if node.left != None:
                left = dfs(node.left) + 1
    
        if left > right:
            return left
        else:
            return right
        
    return dfs(root)