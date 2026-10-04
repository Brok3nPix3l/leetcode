import functools

class Solution:
    def checkValidString(self, s: str) -> bool:
        self.s = s
        
        @cache
        def anyValid(i: int, depth: int) -> bool:
            if i >= len(self.s):
                return depth == 0
            
            cur = self.s[i]
            match cur:
                case '(':
                    return anyValid(i + 1, depth + 1)
                case ')':
                    if depth == 0:
                        return False
                    return anyValid(i + 1, depth - 1)
                case '*':
                    # '('
                    leftParenCanBeValid = anyValid(i + 1, depth + 1)
                    # ')'
                    rightParenCanBeValid = depth > 0 and anyValid(i + 1, depth - 1)
                    # ''
                    emptyStringCanBeValid = anyValid(i + 1, depth)
                    return any((leftParenCanBeValid, rightParenCanBeValid, emptyStringCanBeValid))
        
        return anyValid(0, 0)