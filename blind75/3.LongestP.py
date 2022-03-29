# https://leetcode.com/problems/longest-palindromic-substring/

# use two pointers to go outward for both even and odd amount of chars

def longestPalindrome(s: str) -> str:
        
        result = ''
        length = 0
        
        for i in range(len(s)):
            
            left, right = i, i
            
            #check if it is a palindrome expanding outward
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # r - l + 1 is the difference of where the pointers are
                if (right - left + 1) > length:
                    length = (right - left + 1)
                    result = s[left:right + 1]

                #opposite from normal because we are going outward
                left -= 1
                right += 1
                

            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > length:
                    length = (right - left + 1)
                    result = s[left:right + 1]

                left -= 1
                right += 1
            
            
        return result