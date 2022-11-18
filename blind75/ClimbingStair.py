# https://leetcode.com/problems/climbing-stairs/

# use recursion and a memo

def climbStairs(n: int) -> int:
        
    def recursive(n, memo = {}):
        
        if n in memo:
            return memo[n]
        
        if n < 2:
            return 1
        
        memo[n] = recursive(n-1) + recursive(n-2)
        return memo[n]
    
    return recursive(n)