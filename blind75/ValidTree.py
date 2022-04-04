# https://leetcode.com/problems/validate-binary-search-tree/

# dfs and pass down infinty on either side

def isValidBST(root) -> bool:
        
    def dfs(root, min_val, max_val):
        if not root:
            return True

        if not (min_val < root.val < max_val):
            return False

        return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)

    return dfs(root, -inf, inf) # root is always valid