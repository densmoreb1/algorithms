# https://leetcode.com/problems/unique-paths/

# uses recursion and a memo

def uniquePaths(m: int, n: int) -> int:
        
    def recursion(m, n, memo={}):
        
        key = str(m) + ',' + str(n)
        
        if key in memo:
            return memo[key]
        
        if m == 0 or n == 0:
            return 0
        
        if m == 1 and n == 1:
            return 1
        
        memo[key] = recursion(m-1, n, memo) + recursion(m, n-1, memo)
        return memo[key]
    
    return recursion(m, n)