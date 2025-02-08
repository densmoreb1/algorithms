# https://leetcode.com/problems/design-a-number-container-system
class NumberContainers1:

    def __init__(self):
        self.res = [None]
        self.cont = []
        return None

    def change(self, index: int, number: int) -> None:
        if index > len(self.cont) - 1:
            # need to be filled in
            diff = index - (len(self.cont) - 1)
            for _ in range(diff):
                self.cont.append(-1)

        self.cont[index] = number

        self.res.append(None)
        return None

    def find(self, number: int) -> int:
        for i in range(len(self.cont)):
            if self.cont[i] == number:
                self.res.append(i)
                return i

        self.res.append(-1)
        return -1


class NumberContainers:

    def __init__(self):
        self.res = [None]
        self.cont = {}
        return None

    def change(self, index: int, number: int) -> None:
        self.cont[index] = number
        self.res.append(None)
        return None

    def find(self, number: int) -> int:
        cur_dict = dict(sorted(self.cont.items()))
        sorted_key = list(cur_dict.keys())
        left, right = 0, len(self.cont) - 1
        # binary search
        while left <= right:
            print(left, right)
            mid = (left + right) // 2

            if cur_dict[sorted_key[mid]] == number:
                self.res.append(sorted_key[mid])
                return sorted_key[mid]
            elif cur_dict[sorted_key[mid]] > number:
                right = mid - 1
            else:
                left = mid + 1

        self.res.append(-1)
        return -1


nc = NumberContainers()
nc2 = NumberContainers1()
# cur = [[], [10], [1000000000, 10], [10]]
cur = [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]

for each in cur:
    if each == []:
        continue
    elif len(each) == 1:
        nc.find(each[0])
    elif len(each) == 2:
        nc.change(each[0], each[1])

    print(nc.cont)

print(nc.res)
