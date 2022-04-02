# https://leetcode.com/problems/valid-parentheses/submissions/


def isValid(s: str) -> bool:
    stack = []
    paren_dict = {')': '(',
                    ']': '[',
                    '}': '{'}
    
    for p in s:
        # this only checks the second parenthese
        if p in paren_dict:
            # if the last one matches what the key is then pop it
            if stack and stack[-1] == paren_dict[p]:
                stack.pop()
            else:
                return False
        else:
            # appends the first one
            stack.append(p)
    
    return True if not stack else False