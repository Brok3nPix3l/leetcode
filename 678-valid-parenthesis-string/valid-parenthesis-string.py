import functools

class Solution:
    def checkValidString(self, s: str) -> bool:
        # todo: optimize by making s global and read-only and passing an int with the current index instead of substrings
        return anyValid(s)

@cache
def anyValid(s: str, depth: int=0) -> bool:
    if not s:
        return depth == 0
    
    cur = s[0]
    match cur:
        case '(':
            return anyValid(s[1:], depth + 1)
        case ')':
            if depth == 0:
                return False
            return anyValid(s[1:], depth - 1)
        case '*':
            # '('
            leftParenCanBeValid = anyValid(s[1:], depth + 1)
            # ')'
            rightParenCanBeValid = depth > 0 and anyValid(s[1:], depth - 1)
            # ''
            emptyStringCanBeValid = anyValid(s[1:], depth)
            return any((leftParenCanBeValid, rightParenCanBeValid, emptyStringCanBeValid))