# https://leetcode.com/problems/summary-ranges/description/?envType=problem-list-v2&envId=array


def summary_ranges(arr):

    left, right = 0, 1
    res = []

    while right < len(arr) + 1:

        if arr[right - 1] + 1 == arr[right]:
            right += 1
        else:
            res.append(f"{arr[left]}->{arr[right - 1]}")
            print(f'"{arr[left]}->{arr[right - 1]}"')
            left = right - 1
            right += 1

    return res


nums = [0, 1, 2, 4, 5, 7]
# ["0->2","4->5","7"]
nums = [0, 2, 3, 4, 6, 8, 9]
print(summary_ranges(nums))
