def letter_combinations(digits):

    numbers = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
    }

    def dfs(res, path):
        if len(path) == len(digits):
            res.append(''.join(path))
            return
        
        next = digits[len(path)]
        for letter in numbers[next]:
            path.append(letter)
            dfs(res, path)
            path.pop()

    res = []
    dfs(res, [])

    return res

print(letter_combinations('56'))