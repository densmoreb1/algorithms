# https://www.hackerrank.com/challenges/plus-minus/problem
# find the average of positives and negatives in a list

def plusMinus(arr):
    negative = 0
    positive = 0
    zeros = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zeros += 1

    print(positive / len(arr))
    print(negative / len(arr))
    print(zeros / len(arr))
