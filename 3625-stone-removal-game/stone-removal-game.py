class Solution:
    def canAliceWin(self, n: int) -> bool:
        for i in range(10, 0, -1):
            if n < i:
                return bool(i % 2)
            n -= i

        return False