# https://www.hackerrank.com/challenges/diagonal-difference/problem

# find the difference across the diagonals of a 2d array
def diagonalDifference(arr, n):
    d1 = sum([arr[x][x] for x in range(n)]) 
    d2 = sum([arr[x][n-1-x] for x in range(n)])
    return (abs(d1-d2))