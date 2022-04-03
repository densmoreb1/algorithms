# https://leetcode.com/problems/container-with-most-water/

# use two pointers to move 
def maxArea(height):
    area = 0
    
    #brute force
    
    # for i in range(len(height)):
    #     # start ahead of i
    #     for j in range(i, len(height)):

    #         cur = (j - i) * min(height[i], height[j])
    #         if cur > area:
    #             area = cur

    left = 0
    right = len(height) - 1
    
    while left <= right:
        
        cur = (right - left) * min(height[left], height[right])
        
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
        
        area = max(area, cur)
                
    return area