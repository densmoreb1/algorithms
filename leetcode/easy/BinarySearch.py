# https://leetcode.com/problems/binary-search/description/

def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))

nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(search(nums, target))
