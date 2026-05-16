class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        parity = 0
        ans = [0, 0]
        while n > 0:
            ans[parity] += n & 1
            n >>= 1
            parity = (parity + 1) % 2
        return ans