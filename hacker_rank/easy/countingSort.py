def countingSort(arr):
    # Write your code here
    res = [0] * (len(arr))

    for index, value in enumerate(arr):
        res[value] += 1

    return res[:100]
