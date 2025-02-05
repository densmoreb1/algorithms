# https://leetcode.com/problems/maximum-ascending-subarray-sum


def max_subarray(arr):
    res = arr[0]
    cur = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            cur += arr[i]
        else:
            cur = arr[i]

        res = max(cur, res)

    return res


nums = [10, 20, 30, 5, 10, 50]
print(max_subarray(nums))
