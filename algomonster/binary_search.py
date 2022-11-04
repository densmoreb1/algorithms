# vanilla search
# O(log n)
def vanilla(sorted_list, target):
    l, r = 0, len(sorted_list) - 1 #-1 because len does not include 0

    while l <= r: # sometimes they can end up on the same element
        mid = (l + r) // 2
        if sorted_list[mid] == target:
            return mid
        
        if sorted_list[mid] < target:
            l = mid + 1 # discards the middle because it has been tested
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
            bound = mid # need to be sure it is the first True
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