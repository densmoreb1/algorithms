# https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true
# find the sum of an hourglass shape in the 2d array

arr = [
[-9, -9, -9, 1, 1, 1],
[0,  -9,  0, 4, 3, 2],
[-9, -9, -9, 1, 2, 3],
[0,  0,  8,  6, 6, 0],
[0, 0, 0, -2, 0, 0],
[0, 0, 1,  2, 4, 0]
]

def hourglassSum(arr):
    sum_list = []
    for i in range(len(arr) - 2):
        print(i)
        for j in range(len(arr) - 2):
            sum_list.append(arr[i][j] + arr[i][j+1] + arr[i][j+2]
                                      + arr[i+1][j+1] +
                          arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2] 
            )
    return max(sum_list)


hourglassSum(arr)