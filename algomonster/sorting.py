unsorted = [8, 10, 1, 3, 4, 6, 9, 2, 7, 5]

# insertion sort
# O(n^2)


def insertion(unsorted_list):
    for i in unsorted_list:
        current = i

        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[current]
            current -= 1

    return unsorted_list

# selection sort
# O(n^2)


def selection(unsorted_list):
    for i in range(len(unsorted_list)):
        min_index = i

        for j in range(i, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j

        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]

    return unsorted_list

# bubble sort
# O(n^2)


def bubble(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(len(unsorted_list)):
            if unsorted_list[i] < unsorted_list[j]:
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]

    return unsorted_list

# # merge sort
# # O(2^n)
# def merge(unsorted_list):
#     n = len(unsorted_list)

#     # already sorted / basecase
#     if n <= 1:
#         return unsorted_list

#     mid = n // 2
#     left = merge(unsorted_list[:mid])
#     right = merge(unsorted_list[mid:])

#     l, r = 0, 0
#     res = []
#     while l < mid or r < n - mid:
#         if l == mid:
#             res.append()
