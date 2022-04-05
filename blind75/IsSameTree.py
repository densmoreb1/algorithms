# https://leetcode.com/problems/same-tree/

# recurse down and compare each node

def isSameTree(p, q) -> bool:
        
    if not p and not q:
        return True
    
    if not p or not q:
        return False
    
    if p.val != q.val:
        return False
    
    if isSameTree(p.left, q.left) and isSameTree(p.right, q.right):
        return True