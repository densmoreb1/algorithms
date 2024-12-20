# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# find times of breaking the records min and max

def breakingRecords(scores):
    # probably keep track of a count that raises each time the max changes

    min = max = scores[0]
    count_max = count_min = 0

    for i in scores:
        if i > max:
            max = i
            count_max += 1
        if i < min:
            min = i
            count_min += 1

    return [count_max, count_min]
