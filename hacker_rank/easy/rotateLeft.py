# https://www.hackerrank.com/challenges/array-left-rotation/problem
# rotate items left


def rotateLeft(rotations, arr):
    rotations = rotations % len(arr)
    arr = arr[rotations:] + arr[:rotations]

    return arr


arr = [1, 2, 3, 4, 5]
print(rotateLeft(4, arr))
