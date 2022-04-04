# https://leetcode.com/problems/invert-binary-tree/

def invertTree(tree):

    def dfs(tree):
        if tree is None:
            return None
        return TreeNode(tree.val, dfs(tree.right), dfs(tree.left))
    
    return dfs(tree)