# https://leetcode.com/problems/combination-sum/


# backtracking without repitition
def combinationSum(candidates, target: int):
        
        res = []
        def dfs(nums, starting, remainder, path):
            if remainder == 0:
                res.append(path)
                return 
            
            for i in range(starting, len(nums)):
                num = nums[i]
                if remainder - nums[i] < 0:
                    continue
                dfs(nums, i, remainder - num, path+[num])
        
        dfs(candidates, 0, target, [])
        return res