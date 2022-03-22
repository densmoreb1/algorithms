# https://www.hackerrank.com/challenges/mini-max-sum/problem
# find the least and most amount the list can be added to

def miniMaxSum(arr):
    sum = 0
    max = 0
    min = 2**64
    for x in arr:
        sum += x
        if x > max:
            max = x
        if x < min:
            min = x
    print(sum-max, sum-min)