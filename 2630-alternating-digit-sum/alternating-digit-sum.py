class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        for i, d in enumerate(str(n)):
            if i % 2 == 0:
                ans += int(d)
            else:
                ans -= int(d)
        return ans