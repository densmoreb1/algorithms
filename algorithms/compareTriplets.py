# https://www.hackerrank.com/challenges/compare-the-triplets/problem
# campare two arrays

def compareTriplets(a, b):
    points = [0,0]
    for i in range(0, 3):
        if a[i] > b[i]:
            points[0] += 1
        elif a[i] < b[i]:
            points[1] += 1
    return points