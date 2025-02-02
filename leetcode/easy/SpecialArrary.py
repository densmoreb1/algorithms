# https://leetcode.com/problems/special-array-i

def special_array(arr):

    if len(arr) == 1:
        return True

    for i in range(len(arr) - 1):
        if arr[i] % 2 == arr[i + 1] % 2:
            return False

    return True


nums = [2, 1, 4]
# nums = [4, 3, 1, 6]
print(special_array(nums))
