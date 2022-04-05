# https://leetcode.com/problems/subsets/

# backtracking solution
# keep track of index that you are on with a list
def subsets(nums):
        
    res = []
    subset = []
    
    def dfs(i):
        # base case or reaching the end of the list
        if i >= len(nums):
            res.append(subset.copy())
            return
        
        # include
        subset.append(nums[i])
        dfs(i + 1)
        
        # do not include
        subset.pop()
        dfs(i + 1)
    
    dfs(0)
    return res 