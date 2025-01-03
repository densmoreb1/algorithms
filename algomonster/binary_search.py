# vanilla search
# O(log n)
def vanilla(sorted_list, target):
    l, r = 0, len(sorted_list) - 1  # -1 because len does not include 0

    while l <= r:  # sometimes they can end up on the same element
        mid = (l + r) // 2
        if sorted_list[mid] == target:
            return mid

        if sorted_list[mid] < target:
            l = mid + 1  # discards the middle because it has been tested
        else:
            r = mid - 1

    return -1


# Q1
arr = [False, False, True, True, True]


def find_boundary(arr):
    l, r = 0, len(arr) - 1

    bound = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid]:
            bound = mid  # need to be sure it is the first True
            r = mid - 1
        else:
            l = mid + 1
    return bound

# Q2


def first_not_smaller(arr, target):
    l, r = 0, len(arr) - 1

    bound = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= target:
            bound = mid
            r = mid - 1
        else:
            l = mid + 1
    return bound

# Q3


def first_occurrence(arr, target):
    l, r = 0, len(arr) - 1

    bound = -1
    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == target:
            bound = mid
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return bound

# Q4


def square_root(n):
    if n == 0:
        return 0
    l, r = 0, n

    bound = -1
    while l <= r:
        mid = (l + r) // 2

        if mid * mid == n:  # because it can be spot on
            return mid
        elif mid * mid > n:
            bound = mid
            r = mid - 1
        else:
            l = mid + 1

    return bound - 1  # subtract one if it's bigger

# Q5


def find_min_rotated(arr):
    left, right = 0, len(arr) - 1

    bound = 0
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= arr[-1]:
            bound = mid
            right = mid - 1
        else:
            left = mid + 1

    return bound

# Q6


def peak_mountain(arr):
    pass


print(peak_mountain([0, 1, 2, 3, 2, 1, 0]))
