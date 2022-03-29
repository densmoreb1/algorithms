# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# sliding window while keeping track of count

def longest(s):
    left = 0
    longest = 0
    right = 0
    window = set()
    
    while right < len(s):
        
        if s[right] not in window:
            window.add(s[right])
            right += 1
        else:
            window.remove(s[left])
            left += 1
        
        longest = max(longest, right-left)
    
    return longest