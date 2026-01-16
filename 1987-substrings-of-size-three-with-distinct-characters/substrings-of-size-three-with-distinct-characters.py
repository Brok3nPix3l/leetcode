class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        return sum((1 if (len(set(s[i:i+3])) == 3) else 0) for i in range(len(s) - 2))