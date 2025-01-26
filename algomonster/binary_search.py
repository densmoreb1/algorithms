"""
Base Binary Search
Problem statement:
    Given a sorted array of integers and an integer called target,
    find the element that equals the target and return its index.
    If the element is not found, return -1.
Solution:
    Find the middle of the array
    Is it is the target?
    If it is larger, cut out the right side of the list
    If it is smaller, cut out the left side
"""


def vanilla_search(arr, target):
    left, right = 0, len(arr) - 1
    # <= because left and right could point to the same element, < would miss it
    while left <= right:
        # double slash for integer division in python 3,
        mid = (left + right) // 2
        # found target, return its index
        if arr[mid] == target:
            return mid
        # middle less than target, discard left half by making left search boundary `mid + 1`
        if arr[mid] < target:
            left = mid + 1
        # middle greater than target, discard right half by making right search boundary `mid - 1`
        else:
            right = mid - 1
    return -1  # if we get here we didn't hit above return so we didn't find target


# arr = [1, 3, 5, 7, 8]
# print(vanilla_search(arr, 5))


def find_boundary(arr):
    left, right = 0, len(arr) - 1
    res = -1  # keep where the boundary is

    while left <= right:

        mid = (left + right) // 2
        print(mid)
        if arr[mid]:
            res = mid
            right = mid - 1
        else:
            left = mid + 1

    return res


# find the first True
# arr = [False, False, True, True, True]
# print(find_boundary(arr))

# arr = [True]
# print(find_boundary(arr))


def first_not_smaller(arr, target):
    res = -1
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 1

        if arr[mid] >= target:
            res = mid
            right = mid - 1
        else:
            left = mid + 1

    return res


# arr = [2, 3, 5, 7, 11, 13, 17, 19]
# print(first_not_smaller(arr, 6))  # returns index of 7

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arr = [0]
# print(first_not_smaller(arr, 0))


def find_first_occurrenc(arr, target):
    res = -1
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            res = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1

    return res


arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
target = 1
print(find_first_occurrenc(arr, target))
