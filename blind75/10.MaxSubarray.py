# https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums) -> int:
        
    max_s = nums[0]
    cur = 0
    
    for n in nums:
        if cur < 0:
            cur = 0

        cur += n            
        max_s = max(max_s, cur)

    return max_s
