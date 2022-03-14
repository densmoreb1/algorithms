# https://www.hackerrank.com/challenges/arrays-ds/problem?isFullScreen=true
# reverse an array

def reverseArray(a):
    return a[::-1]

def reverse2(arr):
    reversed_arr = []
    print(arr)
    # range (start, stop, step)
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])

    print(reversed_arr)