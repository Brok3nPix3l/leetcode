class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        found_zero = False
        for i in s[1:]:
            if i == '0':
                found_zero = True
            elif found_zero:
                return False
        return True