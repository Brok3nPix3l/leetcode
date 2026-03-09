class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        for l in "ZYXWVUTSRQPONMLKJIHGFEDCBA":
            if l in s and l.lower() in s:
                return l
        return ""