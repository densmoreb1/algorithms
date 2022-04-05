# https://leetcode.com/problems/house-robber/

def rob(nums) -> int:
        
    rob1, rob2 = 0, 0
    
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    
    return temp