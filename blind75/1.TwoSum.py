# https://leetcode.com/problems/two-sum/

# use a hash map tp keep track of index and value
# or can use two pointers if its sorted

def twoSum(nums, target):
        n_dict = {}
        
        for i in range(len(nums)):
            other_half = target - nums[i]
            
            if other_half in n_dict:
                return [n_dict[other_half], i]
            
            n_dict[nums[i]] = i

def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        
        sum = arr[left] + arr[right]
        
        if sum == target:
            return [left, right]
        
        if sum > target:
            right -= 1
        else:
            left += 1