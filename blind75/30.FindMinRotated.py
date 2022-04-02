# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# use binary search with a boundary with the filter

def findMin(arr):

    left, right = 0, len(arr)-1
    boundary = -1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] <= arr[-1]:
            boundary = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return boundary
