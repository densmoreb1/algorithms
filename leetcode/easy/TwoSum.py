# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):

    nums_dict = {}
    for i in range(len(nums)):
        other_half = target - nums[i]

        if other_half in nums_dict:
            return [nums_dict[other_half], i]
        else:
            nums_dict[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))
