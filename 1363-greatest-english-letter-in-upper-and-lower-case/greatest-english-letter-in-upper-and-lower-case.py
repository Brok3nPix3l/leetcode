import string

class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        for l in string.ascii_uppercase[::-1]:
            if l in s and l.lower() in s:
                return l
        return ""