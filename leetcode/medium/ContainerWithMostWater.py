# https://leetcode.com/problems/container-with-most-water/description/

def most_water(arr):
    right = len(arr) - 1
    left, area = 0, 0

    while left < right:
        new_area = min(arr[left], arr[right]) * (right - left)
        area = max(new_area, area)
        if arr[left] > arr[right]:
            right -= 1
        else:
            left += 1

    return area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(most_water(height))
