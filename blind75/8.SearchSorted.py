# https://leetcode.com/problems/search-in-rotated-sorted-array/


# draw a picture
# first case is if you are in the larger side then search one or the other side

def search(nums, target) -> int:
    
    left, right = 0, len(nums) -1
    
    while left <= right:
        
        mid = (left+right) // 2
        
        if target == nums[mid]:
            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left] > target or nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
    
    return -1