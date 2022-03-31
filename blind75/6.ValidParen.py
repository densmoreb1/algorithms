# https://leetcode.com/problems/valid-parentheses/submissions/


def isValid(s: str) -> bool:
    stack = []
    paren_dict = {')': '(',
                    ']': '[',
                    '}': '{'}
    
    for p in s:
        if p in paren_dict:
            if stack and stack[-1] == paren_dict[p]:
                stack.pop()
            else:
                return False
        else:
            stack.append(p)
    
    return True if not stack else False