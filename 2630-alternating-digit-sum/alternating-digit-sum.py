class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        p = sum(int(d) for d in s[::2])
        n = sum(int(d) for d in s[1::2])
        return p - n