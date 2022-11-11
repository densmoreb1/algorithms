# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# find the count of the max number in the arr

def birthdayCakeCandles(candles):
    max = 0
    count = 0
    for i in candles:
        if max < i:
            max = i
    for i in candles:
        if i >= max:
            count += 1
    return(count)