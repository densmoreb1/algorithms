# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# sliding window while keeping track of count

def longest(s):
    seen = set()
    longest = 0
    
    left = 0
    right = 0
    
    while right < len(s):
        
        if s[right] not in seen:
            # adds new characters
            seen.add(s[right])
            right += 1
        else:
            # removes seen characters
            seen.remove(s[left])
            left += 1

        # right - left gives the space between each letter
        longest = max(longest, right-left)
    return longest