class Solution:
    def maxProduct(self, n: int) -> int:
        a, b = sorted((int(d) for d in str(n)), reverse=True)[:2]
        return a * b