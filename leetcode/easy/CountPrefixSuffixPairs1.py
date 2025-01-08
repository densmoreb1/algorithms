# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i
def countPrefixSuffixPairs(words):
    def isPrefixAndSuffix(str1, str2):
        print('---')
        print(str1, str2)

        front = str2[:len(str1)]
        back = str2[-len(str1):]

        print(front, back)

        if str1 == front and str1 == back:
            return 1
        else:
            return 0

    count = 0

    for i in range(len(words)):
        for j in range(len(words)):
            if i < j:
                count += isPrefixAndSuffix(words[i], words[j])

    return count


words = ["pa", "papa", "ma", "mama"]
print(countPrefixSuffixPairs(words))

words = ["a", "aba", "ababa", "aa"]
print(countPrefixSuffixPairs(words))

words = ["a", "abb"]
print(countPrefixSuffixPairs(words))
