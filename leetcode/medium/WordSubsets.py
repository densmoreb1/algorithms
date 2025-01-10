# https://leetcode.com/problems/word-subsets

# if all of the letters in words2 are in words1 return the word1
def wordSubsets(A, B):
    def count(word):
        ans = [0] * 26
        for letter in word:
            ans[ord(letter) - ord('a')] += 1
        return ans

    bmax = [0] * 26
    for b in B:
        for i, c in enumerate(count(b)):
            bmax[i] = max(bmax[i], c)

    ans = []
    for a in A:
        if all(x >= y for x, y in zip(count(a), bmax)):
            ans.append(a)
    return ans


words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["l", "e"]

# print(word_subsets(words1, words2))

words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["lo", "eo"]

print(wordSubsets(words1, words2))
