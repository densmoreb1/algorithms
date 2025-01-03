from typing import List


class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)


root = build_tree(iter('1 3 2 1 5 0 3 0 4 0'.split()), int)

# Q1


def tree_path(root: Node):
    res = []

    def dfs(node, path):
        if all(c is None for c in node.children):
            res.append('->'.join(path) + '->' + str(node.val))
            return

        for c in node.children:
            if c is not None:
                path.append(str(node.val))
                dfs(c, path)
                path.pop()

    if root:
        dfs(root, [])

    return res


# Q2
def letter_combination(n):
    res = []

    def dfs(s, path):
        if s == n:
            res.append(''.join(path))
            return

        for i in ['a', 'b']:
            path.append(i)
            dfs(s + 1, path)
            path.pop()

    dfs(0, [])
    return res


# Q3
def phone_combinations(digits):
    KEYBOARD = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    res = []

    def dfs(path, start):
        if start == len(digits):
            res.append(''.join(path))
            return

        for digit in KEYBOARD[digits[start]]:
            path.append(digit)
            dfs(path, start + 1)
            path.pop()

    dfs([], 0)
    return res


# Q4
def partitioning(s):
    res = []

    def dfs(path, start):
        print(path, start)
        if start == len(s):
            res.append(path[:])
            return

        for i in range(start + 1, len(s) + 1):  # start at the top and remove letters
            prefix = s[start:i]
            if prefix == prefix[::-1]:
                path.append(prefix)
                dfs(path, i)
                path.pop()

    dfs([], 0)
    return res


print(partitioning('aab'))

# Q5


def generate_parens(n):
    res = []

    def dfs(start, path, open, closed):
        if start == 2 * n:
            res.append(''.join(path))
            return

        if open < n:
            path.append('(')
            dfs(start + 1, path, open + 1, closed)
            path.pop()

        if closed < open:
            path.append(')')
            dfs(start + 1, path, open, closed + 1)
            path.pop()

    dfs(0, [], 0, 0)
    return res


# Q6
def generate_permutations(letters):
    res = []
    used = [False] * len(letters)

    def dfs(length, path: List):
        if length == len(letters):
            res.append(''.join(path))
            return

        for i, letter in enumerate(letters):
            if used[i]:
                continue
            path.append(letter)
            used[i] = True
            dfs(length + 1, path)
            path.pop()
            used[i] = False

    dfs(0, [])
    return res


# Q7
def word_break(s: str, words: list):
    memo = {}

    def dfs(start):
        if start == len(s):
            return True

        if start in memo:
            return memo[start]

        ans = False
        for word in words:
            if s[start:].startswith(word):
                if dfs(start + len(word)):
                    ans = True
                    break
        memo[start] = ans
        return ans

    return dfs(0)


# Q8
def decode_ways(digits: str):
    memo = {}

    def dfs(start: int):
        if start == len(digits):
            return 1

        ways = 0
        if digits[start] == '0':
            return ways

        ways += dfs(start + 1)
        if 10 < int(digits[start: start + 1]) <= 26:
            ways += dfs(start + 2)

        memo[start] = ways
        return ways

    return dfs(0)
