"""
When to use Two Pointers:
    A list that needs to be iterated through
"""


def remove_dupes(arr):
    l = 0

    for r in range(len(arr)):
        if arr[l] != arr[r]:
            l += 1
            arr[l] = arr[r]

    print(arr)
    return l + 1


arr = [0, 0, 1, 1, 1, 2, 2]
print(remove_dupes(arr))
