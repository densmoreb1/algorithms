# https://leetcode.com/problems/word-break/

# depth first search while getting rid of a letter at a time

def wordBreak(s, wordDict) -> bool:
        
    memo = {}
    def dfs(i):
        
        if i == len(s):
            return True
        if i in memo:
            return memo[i]
        
        boolean = False
        for word in wordDict:
            if s[i:].startswith(word):
                if dfs(i+len(word)):
                    boolean = True
                    break
        memo[i] = boolean
        return memo[i]
    
    return dfs(0)