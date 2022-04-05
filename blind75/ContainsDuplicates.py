# https://leetcode.com/problems/contains-duplicate/


def containsDuplicate(nums) -> bool:
        
    vals = {}
    
    for i in nums:
        
        if i in vals:
            if vals[i] >= 1:
                return True
            vals[i] += 1
        else:
            vals[i] = 1
    
    return False