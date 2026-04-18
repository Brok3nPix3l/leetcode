class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        return sum(int(d) for d in s[::2]) - sum(int(d) for d in s[1::2])